from flask import Flask, render_template, redirect, url_for, abort, send_from_directory, request, jsonify, Response
import os
import sys
import subprocess
import threading
import time
import requests
import numpy as np
import cv2
from werkzeug.utils import secure_filename
import mediapipe as mp
import json
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Project configurations
PROJECTS = {
    'gemini_analyzer': {
        'id': 'gemini_analyzer',
        'name': 'Gemini Analyzer',
        'description': 'AI-powered text analysis and processing tool that leverages Google\'s Gemini model for advanced natural language understanding and processing.',
        'path': '/gemini_analyzer',
        'image': 'static/images/gemini.png',
        'port': 5001,
        'tags': ['NLP', 'Text Analysis', 'AI'],
        'features': [
            'Advanced text analysis',
            'Sentiment analysis',
            'Entity recognition',
            'Text summarization'
        ],
        'process': None
    },
    'sign_language': {
        'id': 'sign_language',
        'name': 'Sign Language Translator',
        'description': 'Real-time sign language translation system that converts sign language gestures to text and speech using computer vision and deep learning.',
        'path': '/sign',
        'image': 'static/images/sign.png',
        'port': 4200,
        'tags': ['Computer Vision', 'Real-time', 'Accessibility'],
        'features': [
            'Real-time gesture recognition',
            'Text and speech output',
            'Multiple sign language support',
            'Accessibility features'
        ],
        'process': None
    }
}

# Sign language gesture database
SIGN_LANGUAGE_DB = {
    'hello': {
        'landmarks': [
            # Example landmarks for "hello" sign
            {'x': 0.5, 'y': 0.5, 'z': 0.0},  # Thumb tip
            {'x': 0.6, 'y': 0.5, 'z': 0.0},  # Index tip
            # Add more landmarks for the gesture
        ]
    },
    'thank you': {
        'landmarks': [
            # Example landmarks for "thank you" sign
            {'x': 0.5, 'y': 0.5, 'z': 0.0},  # Thumb tip
            {'x': 0.6, 'y': 0.5, 'z': 0.0},  # Index tip
            # Add more landmarks for the gesture
        ]
    },
    # Add more signs to the database
}

def check_server_health(port):
    """Check if the server is running and healthy"""
    try:
        response = requests.get(f'http://localhost:{port}')
        return response.status_code == 200 or response.status_code == 404
    except:
        return False

@app.route('/')
def home():
    return render_template('index.html', projects=PROJECTS)

@app.route('/gemini_analyzer')
def gemini_analyzer():
    try:
        # Start the server if it's not running
        if not PROJECTS['gemini_analyzer']['process'] or PROJECTS['gemini_analyzer']['process'].poll() is not None:
            os.chdir('gemini_analyzer')
            process = subprocess.Popen([sys.executable, 'main.py'], 
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
            PROJECTS['gemini_analyzer']['process'] = process
            os.chdir('..')
            time.sleep(2)
        # Check if server is healthy
        if check_server_health(PROJECTS['gemini_analyzer']['port']):
            return redirect(f'http://localhost:{PROJECTS["gemini_analyzer"]["port"]}/gemini-analyzer')
        else:
            abort(503, description="Gemini Analyzer service is starting up. Please try again in a few seconds.")
    except Exception as e:
        abort(503, description=f"Gemini Analyzer service is currently unavailable: {str(e)}")

@app.route('/sign')
def sign_language():
    try:
        # Start the sign language service if it's not running
        if not check_server_health(PROJECTS['sign_language']['port']):
            os.chdir('sign/Sign-Language-to-Text-Speech-master')
            # Install dependencies if needed
            if not os.path.exists('node_modules'):
                subprocess.run(['npm', 'install'], shell=True)
            # Start the Angular development server with the correct configuration
            process = subprocess.Popen(['ng', 'serve', '--port', str(PROJECTS['sign_language']['port'])], 
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     shell=True)
            PROJECTS['sign_language']['process'] = process
            os.chdir('../../')
            time.sleep(10)  # Give the service more time to start
        
        # Redirect to the Angular app's translation page
        return redirect(f'http://localhost:{PROJECTS["sign_language"]["port"]}/translate')
    except Exception as e:
        abort(503, description=f"Sign Language service is currently unavailable: {str(e)}")

@app.route('/video_feed')
def video_feed():
    """Video streaming route for webcam input"""
    try:
        return Response(generate_frames(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        print(f"Error in video feed: {str(e)}")
        return str(e), 500

def generate_frames():
    """Generate video frames with sign language detection"""
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise Exception("Could not open camera")
        
    try:
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                # Convert to RGB for MediaPipe
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(rgb_frame)
                
                # Draw hand landmarks and get translation
                translation = "No hand detected"
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing = mp.solutions.drawing_utils
                        mp_drawing.draw_landmarks(
                            frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                        
                        # Process hand landmarks for sign language detection
                        landmarks = []
                        for landmark in hand_landmarks.landmark:
                            landmarks.append({
                                'x': landmark.x,
                                'y': landmark.y,
                                'z': landmark.z
                            })
                        
                        # Get translation
                        translation = process_hand_landmarks(landmarks)
                
                # Display translation on frame
                cv2.putText(frame, translation, (10, 30),
                          cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    finally:
        camera.release()

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        source_type = request.form.get('source_type')
        prompt = request.form.get('prompt', 'Describe what you see in this media.')
        
        if source_type == 'url':
            source = request.form.get('url')
            if not source:
                return jsonify({'error': 'URL is required'}), 400
            result = process_input(source, prompt)
        elif source_type == 'youtube':
            source = request.form.get('youtube_url')
            if not source:
                return jsonify({'error': 'YouTube URL is required'}), 400
            result = process_input(source, prompt)
        elif source_type == 'file':
            if 'file' not in request.files:
                return jsonify({'error': 'No file uploaded'}), 400
            file = request.files['file']
            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            try:
                result = process_input(filepath, prompt)
            finally:
                if os.path.exists(filepath):
                    os.remove(filepath)
        else:
            return jsonify({'error': 'Invalid source type'}), 400
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze_sign', methods=['POST'])
def analyze_sign():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Save the image temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Process the image using MediaPipe
            image = cv2.imread(filepath)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_image)
            
            if results.multi_hand_landmarks:
                # Send the image to the sign language translation service
                translation_url = f'http://localhost:{PROJECTS["sign_language"]["port"]}/api/translate'
                files = {'image': open(filepath, 'rb')}
                response = requests.post(translation_url, files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    return jsonify(result)
                else:
                    return jsonify({
                        'error': 'Failed to get translation from sign language service'
                    }), 500
            else:
                return jsonify({
                    'result': 'No hand detected in the image',
                    'confidence': 0.0
                })
        finally:
            # Clean up the temporary file
            if os.path.exists(filepath):
                os.remove(filepath)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def process_hand_landmarks(landmarks):
    """
    Process hand landmarks to detect sign language gestures
    """
    try:
        if not landmarks:
            return "No hand detected"

        # Convert landmarks to a format suitable for comparison
        current_landmarks = np.array([[lm['x'], lm['y'], lm['z']] for lm in landmarks])
        
        # Compare with known signs
        best_match = None
        best_similarity = -1
        
        for sign, data in SIGN_LANGUAGE_DB.items():
            known_landmarks = np.array([[lm['x'], lm['y'], lm['z']] for lm in data['landmarks']])
            
            # Ensure both arrays have the same shape
            if current_landmarks.shape == known_landmarks.shape:
                # Calculate similarity
                similarity = cosine_similarity(current_landmarks, known_landmarks)[0][0]
                
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_match = sign
        
        # Return the best match if similarity is above threshold
        if best_similarity > 0.8:  # Adjust threshold as needed
            return best_match
        else:
            return "Unknown sign"
            
    except Exception as e:
        print(f"Error processing landmarks: {str(e)}")
        return "Error processing sign"

@app.route('/text_to_sign', methods=['POST'])
def text_to_sign():
    """Convert text to sign language representation"""
    try:
        text = request.json.get('text', '')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Use the sign language translation service
        translation_url = f'http://localhost:{PROJECTS["sign_language"]["port"]}/api/text-to-sign'
        response = requests.post(translation_url, json={'text': text})
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({
                'error': 'Failed to convert text to sign language'
            }), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/static/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.errorhandler(503)
def service_unavailable(e):
    return render_template('error.html', error=str(e)), 503

def cleanup():
    """Cleanup function to stop all model servers"""
    for model_id, project in PROJECTS.items():
        if project['process'] and project['process'].poll() is None:
            project['process'].terminate()
            project['process'].wait()

if __name__ == '__main__':
    try:
        app.run(debug=True, port=5000)
    finally:
        cleanup() 