# IBM_FinalProject

# 🧠 AI-Prompt-Story-Generator (Gemini + Gradio)

A simple web app that generates short, creative stories from user prompts using **Google's Gemini model** (via `google-generativeai`) and **Gradio**. Perfect for exploring creative writing with the help of Generative AI.

---

## 📖 AI Story Generator

An interactive app where you input a story prompt (like *“A robot who dreams of being human”*) and Gemini generates a unique, imaginative story in response.

---

## 🧰 Tools Used
- Python
- [Gradio](https://gradio.app/) (UI)
- [Google Generative AI SDK](https://pypi.org/project/google-generativeai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (for API key management)

---

## 🚀 How to Run the App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/AI-Prompt-Story-Generator.git
   cd AI-Prompt-Story-Generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Gemini API Key:**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. **Run the app:**
   ```bash
   python app.py
   ```

5. The app will launch at [http://localhost:7860](http://localhost:7860)

---

## 🖼️ Example Prompts
- "A lonely robot explores Mars"
- "A tiger who writes poetry"
- "A girl discovers a magical clock tower"

---

## ✅ Features
- Custom story generation from any prompt
- Simple, clean UI via Gradio
- Automatically handles API errors
- Gemini-powered for fast and creative results
