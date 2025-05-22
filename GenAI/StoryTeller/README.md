# 📚 Children's Story Generator (TinyLLaMA + FastAPI)

Create magical children's stories with AI! This project uses the lightweight **TinyLLaMA-1.1B-Chat** model served via **FastAPI** and accessed through a friendly **frontend web page**. It leverages **ngrok** to expose the backend for easy public access.

---

## 🌟 Features

- ✨ Generate unique children's stories based on heartwarming themes like Friendship, Bravery, Kindness, and more
- 🧠 Powered by TinyLLaMA — a small, fast language model
- 🚀 Backend: FastAPI with ngrok tunnel
- 🎨 Frontend: Light-yellow themed web interface for kids
- 📡 Easy deployment and testing via public ngrok URL

---

## 🛠️ Requirements

Install the required Python libraries:

```bash
pip install transformers accelerate torch fastapi uvicorn pyngrok
