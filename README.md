# ♻️ WasteBot: AI-Powered Waste Segregation

WasteBot is an end-to-end solution designed to simplify waste management using **Computer Vision** and **Natural Language Processing**. This project aims to educate users on proper disposal techniques through an interactive, gamified platform.

> **💡 Project Milestone:** This project was developed during my **B.Tech 1st Semester**. It was built **100% using AI (ChatGPT)**, demonstrating the power of AI-assisted engineering to create complex, multi-layered software solutions without prior detailed knowledge of the full stack.



## 🚀 Key Features

* **Image Classification:** Leverages a **ResNet18** Deep Learning model to identify waste categories from uploaded images.
* **Text Classification:** Uses a **Zero-Shot Classification** model (`facebook/bart-large-mnli`) to categorize waste based on text descriptions.
* **Dual-Interface Support:** * **Streamlit Dashboard:** A data-centric Python interface for quick classification and leaderboard viewing.
    * **Web Portal:** A traditional HTML/CSS/JS frontend for a seamless, visually appealing user experience.
* **Gamification:** A leaderboard and reward system that awards points to users for engaging with sustainable practices.

## 🏗️ Project Architecture

The project is built using a modular architecture to separate logic from presentation:

1. **Backend (`backend.py`):** A Flask-based API that serves as the central hub. It processes image bytes, runs text inference via Hugging Face, and handles the leaderboard logic.
2. **Frontend Options:**
    * **Pythonic (`front.py`):** Built with Streamlit for rapid prototyping and easy visualization.
    * **Web-Standard (`index.html`, `style.css`, `script.js`):** A custom-styled landing page using CSS gradients and JavaScript to simulate API interactions.
3. **AI Engine (`dataset.py`):** Handles model initialization and ensures the environment is ready for inference.

## 📂 File Description

| File | Role |
| :--- | :--- |
| `backend.py` | The "Brain." Flask server containing routes for classification and leaderboard. |
| `front.py` | Streamlit UI code. Provides file uploaders and text input fields. |
| `index.html` | The main structure of the web-based landing page. |
| `style.css` | Professional styling using Flexbox, gradients, and responsive design. |
| `script.js` | Handles UI interactions on the web portal. |
| `dataset.py` | Utility script to verify successful loading of the ResNet18 model. |

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have Python installed. Install the required libraries using:
```bash
pip install flask flask-cors torch torchvision pillow transformers streamlit requests
