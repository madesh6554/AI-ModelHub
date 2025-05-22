from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os
from processor import process_input  # Your existing code

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_media(
    prompt: str = Form(...),
    file: UploadFile = File(None),
    url: str = Form(None)
):
    try:
        if file:
            temp_path = f"temp_{file.filename}"
            with open(temp_path, "wb") as buffer:
                buffer.write(await file.read())
            
            result = process_input(temp_path, prompt)
            os.remove(temp_path)
            return {"result": result}
        
        if url:
            return {"result": process_input(url, prompt)}
        
        return {"error": "No input provided"}
    
    except Exception as e:
        return {"error": str(e)}