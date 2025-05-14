# AI Model Hub

## Overview
AI Model Hub is a comprehensive platform that combines two powerful AI applications:
1. **Gemini Analyzer**: An AI-powered media analysis tool
2. **Sign Language Translation**: A real-time sign language detection and translation system

## Projects

### 1. Gemini Analyzer
- Media analysis using Google's Gemini AI
- Support for images, videos, and YouTube content
- Real-time processing and analysis
- [View Gemini Analyzer Documentation](gemini_analyzer/README.md)

### 2. Sign Language Translation
- Real-time sign language detection
- Gesture to text conversion
- Text-to-speech output
- [View Sign Language Documentation](sign/README.md)

## Features
- **Unified Interface**: Seamless navigation between both applications
- **Modern Design**: Clean and intuitive user interface
- **Real-time Processing**: Instant analysis and translation
- **Multiple Input Methods**: Support for various media types and sources

## Technical Stack
- **Frontend**: 
  - HTML5, TailwindCSS, JavaScript (Gemini Analyzer)
  - Angular, Ionic Framework (Sign Language)
- **Backend**: FastAPI (Python)
- **AI/ML**: 
  - Google Gemini AI
  - MediaPipe
  - OpenCV
  - Custom ML models

## Setup and Installation
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the FastAPI server:
```bash
python main.py
```

3. Access the applications:
   - Gemini Analyzer: `http://localhost:8000/gemini`
   - Sign Language: `http://localhost:8000/sign`

## Usage
1. Choose the desired application from the navigation
2. Follow the specific instructions for each application
3. View results and analysis in real-time

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 