# 🥗 AI Diet Planner with FastAPI and Phi-2

This project is an AI-powered diet planning API built using [Microsoft's Phi-2](https://huggingface.co/microsoft/phi-2) language model via Hugging Face Transformers. It uses FastAPI for the backend and generates personalized one-day meal plans based on user goals such as "Weight Loss", "Balanced Diet", "Muscle Gain", etc.

## 🌐 Demo

You can interact with the model using a simple HTML frontend that communicates with the FastAPI backend hosted through **ngrok**.

---

## 🚀 Features

- Uses Phi-2 model to generate structured meal plans.
- Returns only the relevant parts: **Breakfast**, **Lunch**, **Dinner**, **Snack**.
- FastAPI-based backend API.
- Accessible via a public `ngrok` URL.
- Frontend built with pure HTML + JS (no frameworks).

---

## 📦 Dependencies

Install the required packages (in Google Colab or locally):

```bash
pip install transformers accelerate fastapi uvicorn nest-asyncio pyngrok

