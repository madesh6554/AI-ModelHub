
# AI ModelHub

## 🔍 Overview
**AI ModelHub** by **Team Quantum Integrators** is a unified AI interface that brings together **10 advanced models** across five major domains:

- 🧠 Natural Language Processing (NLP)
- 👁️ Computer Vision
- 🎧 Audio/Speech Processing
- 🤖 Generative AI
- 🔀 Multimodal AI

This repository serves as a central hub for exploring, testing, and extending the capabilities of various AI-powered tools through a user-friendly web interface.

---

## 💡 Domains & Projects

### 🧠 1. Natural Language Processing (NLP)
NLP is used to analyze, interpret, and generate human language. Our NLP tools include:

- **Text Classification**: Automatically categorize texts (e.g., spam detection, topic labeling)
- **Named Entity Recognition (NER)**: Extract people, places, and organizations from text
- **Sentiment Analysis**: Understand emotions behind user-generated content
- **Text Summarization**: Generate concise summaries from long documents
- **Question Answering**: Answer questions using context from paragraphs

**Tech Stack:**  
OpenAI GPT, spaCy, NLTK, Hugging Face Transformers

---

### 🎧 2. Audio / Speech Processing
Audio models convert spoken language into text and vice versa.

- **Speech-to-Text**: Convert user speech into written commands (powered by OpenAI Whisper)
- **Text-to-Speech**: Convert AI-generated text into spoken audio (using pyttsx3 or gTTS)
- **Speaker Emotion Detection** *(optional feature)*: Analyze tone to determine speaker mood

**Use Cases:**  
Virtual assistants, accessibility tools, voice-operated systems

---

### 👁️ 3. Computer Vision
Computer Vision models analyze images and extract meaningful information.

- **Image Classification**: Detect object categories in images
- **Object Detection**: Identify and locate multiple objects in a frame
- **Face Detection & Emotion Recognition** *(optional features)*
- **Scene Understanding**: Use foundation models to explain complex visuals

**Libraries Used:**  
OpenCV, TensorFlow/Keras, MediaPipe

---

### 🤖 4. Generative AI
These models **generate new content** based on prompts.

- **Text Generation**: Create stories, summaries, or code using language models
- **Image Generation** *(optional)*: Generate images from text (e.g., DALL·E)
- **Style Transfer** *(Vision-to-Vision)*: Transform visual art into another style

**Backends:**  
OpenAI GPT, Gemini Pro, Hugging Face LLMs

---

### 🔀 5. Multimodal AI
Multimodal AI allows **multiple input types** (text + image + voice) to be processed simultaneously to produce intelligent responses.

#### 📌 This section is powered by two foundation models:
- **Google Gemini Pro Vision**
- **OpenAI GPT-4 with Vision (GPT-4V)**

#### 💻 Features:
- **Multiple Inputs Supported:**
  - 📷 **Image Upload**
  - ⌨️ **Text Input**
  - 🎙️ **Voice Input** (transcribed via Whisper)
- **Smart Response Generation**:
  - Combines image + question for insightful analysis
  - Handles OCR-like queries and content recognition

#### 🧠 Use Cases:
- "What is in this image?"
- "Summarize the content of this receipt"
- "Read and explain this chart"
- "Voice question + image analysis"

#### 🛠 Tools and Libraries:
- FastAPI (backend)
- OpenAI API (Whisper, GPT-4V)
- Gemini Pro Vision API
- OpenCV, pyttsx3

🔗 [View Multimodal README](Mutimodal/README.md)

---

## 🌐 Features
- 🔗 Unified platform to test 10+ models
- ⚡ Real-time performance on all models
- 🎨 Modern, responsive UI with Angular & TailwindCSS
- 🧩 Modular architecture for easy expansion
- 📱 Cross-platform: works on desktop & mobile

---

## 🧰 Tech Stack

| Layer         | Tools & Frameworks                               |
|---------------|--------------------------------------------------|
| Frontend      | HTML5, TailwindCSS, JavaScript, Angular, Ionic   |
| Backend       | Python, FastAPI                                  |
| AI/ML Models  | Gemini Pro, GPT-4V, Whisper, OpenCV, MediaPipe   |
| Speech        | pyttsx3, OpenAI Whisper                          |
| Dev Tools     | Git, VS Code, GitHub                             |

---

## 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/madesh6554/AI-ModelHub.git
   cd AI-ModelHub
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend server**
   ```bash
   python main.py
   ```

4. **Access the web app**
   - Gemini Analyzer: `http://localhost:8000/gemini`
   - Sign Language: `http://localhost:8000/sign`
   - Multimodal: `http://localhost:8000/multimodal`

---

## 🧪 Usage

1. Select the desired domain from the UI
2. Provide input: text, image, or voice
3. View AI-generated results in real-time

---

## 🤝 Contributing

We welcome your contributions!

1. Fork the repo
2. Create a branch
3. Make your changes
4. Submit a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for more details.

---

## 👨‍💻 Team Quantum Integrators
> “Bringing together the best of AI under one unified roof.”
