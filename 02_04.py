from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# -------------------------
# 1️⃣ Gemini AI setup (FIXED)
# -------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("⚠️ GEMINI_API_KEY not found! Set it in your .env file")

# Configure with correct API version
genai.configure(api_key=GEMINI_API_KEY)

# Use the correct model name
model = genai.GenerativeModel('models/gemini-2.0-flash-001')

# -------------------------
# 2️⃣ Prompt template
# -------------------------
GLOBAL_PROMPT_TEMPLATE = """
You are a friendly, intelligent AI assistant named Mr.A. You provide detailed, 
comprehensive answers (4-7 lines minimum) to any question. You can:
- Explain concepts thoroughly with examples
- Extract and analyze data from text
- Provide step-by-step guidance
- Engage in meaningful conversations

Question: {question}

Provide a detailed answer:
"""

# -------------------------
# 3️⃣ Chatbot logic
# -------------------------
def query_llm(question):
    try:
        prompt_text = GLOBAL_PROMPT_TEMPLATE.format(question=question)
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        return f"I encountered an error: {str(e)}. Please check your API key and try again!"

# -------------------------
# 4️⃣ Flask routes
# -------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    question = data.get("question", "")
    
    if not question:
        return jsonify({"response": "Please ask me something!"})
    
    answer = query_llm(question)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)