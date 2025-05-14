from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from processor import process_input
import os

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def home():
    return send_from_directory('.', 'home.html')

@app.route('/gemini-analyzer')
def gemini_analyzer():
    return send_from_directory('.', 'index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_media():
    try:
        data = request.json
        source = data.get('source')
        prompt = data.get('prompt')
        
        if not source or not prompt:
            return jsonify({'error': 'Missing source or prompt'}), 400
            
        result = process_input(source, prompt)
        return jsonify({'result': result})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
            
        file = request.files['file']
        prompt = request.form.get('prompt')
        
        if not file or not prompt:
            return jsonify({'error': 'Missing file or prompt'}), 400
            
        # Save the file temporarily
        temp_path = os.path.join('temp', file.filename)
        os.makedirs('temp', exist_ok=True)
        file.save(temp_path)
        
        # Process the file
        result = process_input(temp_path, prompt)
        
        # Clean up
        os.remove(temp_path)
        
        return jsonify({'result': result})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 