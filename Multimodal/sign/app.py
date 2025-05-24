from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='Sign-Language-to-Text-Speech-master/dist')

@app.route('/')
def serve_angular():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/health')
def health_check():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(debug=True, port=5002) 