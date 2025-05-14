from fastapi import FastAPI, UploadFile, File, HTTPException, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import cv2
import numpy as np
import mediapipe as mp
from datetime import datetime
import shutil
import json
from typing import Optional
import requests
from gemini_analyzer.processor import process_input

app = FastAPI(title="AI Model Hub")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Create necessary directories
os.makedirs("uploads", exist_ok=True)
os.makedirs("static", exist_ok=True)

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about/gemini", response_class=HTMLResponse)
async def about_gemini(request: Request):
    return templates.TemplateResponse("about_gemini.html", {"request": request})

@app.get("/about/sign", response_class=HTMLResponse)
async def about_sign(request: Request):
    return templates.TemplateResponse("about_sign.html", {"request": request})

@app.get("/docs", response_class=HTMLResponse)
async def docs(request: Request):
    return templates.TemplateResponse("docs.html", {"request": request})

@app.get("/docs/gemini", response_class=HTMLResponse)
async def docs_gemini(request: Request):
    return templates.TemplateResponse("docs_gemini.html", {"request": request})

@app.get("/docs/sign", response_class=HTMLResponse)
async def docs_sign(request: Request):
    return templates.TemplateResponse("docs_sign.html", {"request": request})

@app.get("/gemini", response_class=HTMLResponse)
async def gemini(request: Request):
    return templates.TemplateResponse("gemini_analyzer.html", {"request": request})

@app.get("/sign", response_class=HTMLResponse)
async def sign(request: Request):
    return templates.TemplateResponse("sign_language.html", {"request": request})

@app.post("/api/upload")
async def upload_video(
    file: UploadFile = File(None),
    youtube_url: str = Form(None),
    prompt: str = Form(None)
):
    # Use Gemini's process_input for all cases
    if file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{file.filename}"
        file_path = os.path.join("uploads", filename)
        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            result = process_input(file_path, prompt or "Describe this media")
            os.remove(file_path)
            return {"result": result}
        except Exception as e:
            if os.path.exists(file_path):
                os.remove(file_path)
            raise HTTPException(status_code=500, detail=str(e))
    elif youtube_url:
        url = youtube_url.strip()
        # If it's a direct image or video URL or YouTube URL, just pass to process_input
        try:
            result = process_input(url, prompt or "Describe this media")
            return {"result": result}
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing URL: {str(e)}")
    else:
        raise HTTPException(status_code=400, detail="No file or URL provided.")

def process_image(file_path: str):
    """Process uploaded image file"""
    try:
        # Read the image
        image = cv2.imread(file_path)
        if image is None:
            raise Exception("Could not read image file")
        
        # Convert to RGB for MediaPipe
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_image)
        
        # Count hand detections
        hand_count = len(results.multi_hand_landmarks) if results.multi_hand_landmarks else 0
        
        return {
            "total_frames": 1,
            "hand_detections": hand_count,
            "average_hands_per_frame": hand_count
        }
    except Exception as e:
        raise Exception(f"Error processing image: {str(e)}")

def process_video(file_path: str):
    """Process uploaded video file"""
    try:
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            raise Exception("Could not open video file")

        frame_count = 0
        hand_count = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            # Convert to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)
            
            if results.multi_hand_landmarks:
                hand_count += len(results.multi_hand_landmarks)
            
            frame_count += 1
        
        cap.release()
        
        return {
            "total_frames": frame_count,
            "hand_detections": hand_count,
            "average_hands_per_frame": hand_count / frame_count if frame_count > 0 else 0
        }
    except Exception as e:
        raise Exception(f"Error processing video: {str(e)}")

@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

@app.exception_handler(500)
async def server_error_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("500.html", {"request": request}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 