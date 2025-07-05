import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini with API key
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Function to generate story
def generate_story(prompt):
    if not prompt.strip():
        return "⚠ Please enter a story prompt."
    
    try:
        response = model.generate_content(
            f"Write a short, creative story based on this prompt: {prompt}. Keep it under 300 words."
        )
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating story: {e}"

# Gradio Interface
iface = gr.Interface(
    fn=generate_story,
    inputs=gr.Textbox(
        lines=2,
        label="📝 Enter a Story Prompt",
        placeholder="e.g., A time traveler visits ancient Egypt"
    ),
    outputs=gr.Textbox(label="📖 Your AI-Generated Story"),
    title="📚 AI Story Generator",
    description="Type a prompt and Gemini will write a short story for you!",
    examples=[
        ["A dragon that lost its fire"],
        ["A cat who becomes president"],
        ["A scientist who accidentally builds a talking plant"]
    ]
)

# Launch the app
iface.launch(debug=True)
