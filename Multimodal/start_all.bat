@echo off
echo Starting AI ModelHub services...

:: Start the FastAPI application
start cmd /k "python main.py"

:: Start the sign language application
start cmd /k "cd sign\Sign-Language-to-Text-Speech-master && npm start"

echo Services started! Please wait for all windows to initialize...
echo FastAPI server will be available at: http://localhost:8000
echo Sign Language application will be available at: http://localhost:3000 