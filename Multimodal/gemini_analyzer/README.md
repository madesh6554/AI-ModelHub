# Gemini Analyzer

## Overview
Gemini Analyzer is an AI-powered media analysis tool that leverages Google's Gemini AI to analyze images, videos, and YouTube content. The application provides a modern, user-friendly interface for uploading and analyzing various types of media content.

## Features
- **Media Upload**: Support for both file uploads and YouTube URL inputs
- **Real-time Analysis**: Instant processing of uploaded media
- **Multiple Media Types**: Support for images and videos
- **Interactive Interface**: Drag-and-drop functionality and real-time previews
- **Detailed Analysis**: Comprehensive analysis results with visual feedback

## Technical Stack
- **Frontend**: HTML5, TailwindCSS, JavaScript
- **Backend**: FastAPI (Python)
- **AI Integration**: Google Gemini AI
- **Video Processing**: OpenCV
- **Media Handling**: YouTube API integration

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
1. Upload media through drag-and-drop or file selection
2. Or enter a YouTube URL for analysis
3. Add an analysis prompt (optional)
4. Click "Analyze Media" to process
5. View results in the preview section

## API Endpoints
- `/api/upload`: Upload and analyze media files
- `/api/analyze`: Analyze media from URLs

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 