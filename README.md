# 🤖 Flask Gemini Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![Gemini API](https://img.shields.io/badge/Gemini-API-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**A powerful AI chatbot powered by Google's Gemini API and Flask**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [API Reference](#-api-reference) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Customization](#-customization)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🌟 Overview

Flask Gemini Chatbot is a modern, lightweight web application that leverages Google's powerful Gemini AI model to create an intelligent conversational assistant. Built with Flask and Python, this chatbot provides a seamless user experience with real-time responses and a clean, intuitive interface.

Whether you're looking to integrate AI capabilities into your application, learn about AI APIs, or create your own custom chatbot, this project serves as an excellent starting point.

![Project Logo](assets/logo.png)


---

## ✨ Features

- 🚀 **Real-time AI Responses** - Instant replies powered by Google's Gemini API
- 💬 **Conversational Interface** - Clean and intuitive chat UI
- 🔒 **Secure API Key Management** - Environment-based configuration
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- 🎨 **Customizable UI** - Easy to theme and modify
- ⚡ **Fast & Lightweight** - Minimal dependencies, maximum performance
- 🔄 **Session Management** - Maintains conversation context
- 🛡️ **Error Handling** - Robust error management and user feedback

---

## 🛠️ Tech Stack

- **Backend**: Python 3.8+, Flask 3.0+
- **AI Model**: Google Gemini API
- **Frontend**: HTML5, CSS3, JavaScript
- **HTTP Client**: Fetch API
- **Environment Management**: python-dotenv

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- A Google Gemini API key ([Get one here](https://ai.google.dev/))

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/abinasharma001/flask-gemini-chatbot.git
cd flask-gemini-chatbot
```

### 2. Create a Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
touch .env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ⚙️ Configuration

### Obtaining Your Gemini API Key

1. Visit [Google AI Studio](https://ai.google.dev/)
2. Sign in with your Google account
3. Navigate to "Get API Key"
4. Create a new project or select an existing one
5. Copy your API key and add it to the `.env` file

### Configuration Options

You can customize various settings in `app.py`:

```python
# Model Configuration
MODEL_NAME = "gemini-pro"  # or "gemini-pro-vision" for image support

# Server Configuration
DEBUG = True  # Set to False in production
HOST = "0.0.0.0"
PORT = 5000
```

---

## 💻 Usage

### Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000` (or `http://127.0.0.1:5000`)

### Using the Chatbot

1. Open your web browser and navigate to `http://localhost:5000`
2. Type your message in the input field
3. Press **Enter** or click the **Send** button
4. Receive AI-powered responses instantly!

---

## 📁 Project Structure

```
flask-gemini-chatbot/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
├── .gitignore             # Git ignore file
│
├── static/                # Static files
│   ├── css/
│   │   └── style.css      # Custom styles
│   ├── js/
│   │   └── script.js      # Frontend JavaScript
│   └── images/            # Images and icons
│
├── templates/             # HTML templates
│   └── index.html         # Main chat interface
│
└── README.md              # Project documentation
```

---

## 🔌 API Endpoints

### `GET /`
- **Description**: Renders the main chat interface
- **Response**: HTML page

### `POST /chat`
- **Description**: Sends a message to the Gemini API and returns the response
- **Request Body**:
  ```json
  {
    "message": "Your message here"
  }
  ```
- **Response**:
  ```json
  {
    "response": "AI generated response"
  }
  ```

### `POST /clear`
- **Description**: Clears the current chat session
- **Response**:
  ```json
  {
    "status": "success",
    "message": "Chat cleared"
  }
  ```

---

## 🎨 Customization

### Modifying the UI

Edit `static/css/style.css` to change the appearance:

```css
/* Change chat bubble colors */
.user-message {
    background-color: #007bff;
}

.bot-message {
    background-color: #f1f3f5;
}
```

### Adjusting AI Behavior

Modify the system prompt in `app.py`:

```python
generation_config = {
    "temperature": 0.9,  # Creativity (0.0-1.0)
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'google.generativeai'`

**Solution**: Make sure you've activated your virtual environment and installed all dependencies:
```bash
pip install -r requirements.txt
```

---

**Issue**: `API Key Error: Invalid API key`

**Solution**: 
1. Verify your API key is correct in the `.env` file
2. Ensure there are no extra spaces or quotes
3. Check that your API key is active in Google AI Studio

---

**Issue**: `Rate Limit Exceeded`

**Solution**: The Gemini API has rate limits (60 requests/minute). If you hit this:
1. Wait a minute before trying again
2. Implement request throttling in your code
3. Consider upgrading your API quota

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly before submitting

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Google** for the powerful Gemini API
- **Flask** team for the excellent web framework
- **Open Source Community** for inspiration and support
- All **contributors** who help improve this project

---

## 📞 Contact & Support

- **Author**: Abina Sharma
- **Repository**: [flask-gemini-chatbot](https://github.com/abinasharma001/flask-gemini-chatbot)
- **Issues**: [Report a bug](https://github.com/abinasharma001/flask-gemini-chatbot/issues)

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/abinasharma001/flask-gemini-chatbot?style=social)
![GitHub forks](https://img.shields.io/github/forks/abinasharma001/flask-gemini-chatbot?style=social)
![GitHub issues](https://img.shields.io/github/issues/abinasharma001/flask-gemini-chatbot)

---

<div align="center">

**Made with ❤️ and Python**

If you find this project helpful, please consider giving it a ⭐!

</div>
