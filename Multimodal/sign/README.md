# Sign Language Translation

## Overview
Sign Language Translation is an AI-powered application that converts sign language gestures into text and speech. The application uses computer vision and machine learning to detect and interpret sign language gestures in real-time.

## Features
- **Real-time Sign Detection**: Instant recognition of sign language gestures
- **Video Processing**: Support for both live camera feed and video uploads
- **Text Output**: Conversion of signs to text
- **Speech Synthesis**: Text-to-speech conversion of detected signs
- **Multi-hand Detection**: Support for detecting multiple hands simultaneously

## Technical Stack
- **Frontend**: Angular, Ionic Framework
- **Backend**: FastAPI (Python)
- **Computer Vision**: MediaPipe, OpenCV
- **Machine Learning**: Custom sign language detection models
- **Speech Synthesis**: Text-to-speech integration

## Setup and Installation
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the FastAPI server:
```bash
python main.py
```

3. Access the application at `http://localhost:8000`

## Usage
1. Start the camera or upload a video
2. Perform sign language gestures
3. View real-time translation
4. Listen to speech output (optional)

## API Endpoints
- `/api/upload`: Upload and process sign language videos
- `/api/analyze`: Analyze sign language from video sources
- `/api/detect`: Real-time sign language detection

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 