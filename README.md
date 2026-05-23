# 🌐 English to Indian & World Language Translator

A **Flask-based web application** that translates English text into multiple Indian and world languages using the Google Translate API (via `deep-translator`). Supports both a browser-based UI and a command-line interface.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey?logo=flask)
![deep-translator](https://img.shields.io/badge/deep--translator-Google%20Translate-green)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-46E3B7?logo=render)](https://language-translator-1waf.onrender.com)

## 🔗 Live Demo

👉 **[https://language-translator-1waf.onrender.com](https://language-translator-1waf.onrender.com)**

---

## ✨ Features

- 🔤 Translate English text into **13 languages** including Indian regional languages
- 🌍 Supported languages:
  - **Indian**: Kannada, Hindi, Tamil, Telugu, Malayalam, Bengali, Marathi, Gujarati
  - **International**: Spanish, French, German, Chinese, Arabic
- 🖥️ Clean web UI served via Flask
- ⌨️ CLI tool for quick terminal-based translations
- 🔌 REST API endpoint for programmatic access
- ☁️ Ready to deploy on **Render** or **Vercel**

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11, Flask, Flask-CORS |
| Translation | [deep-translator](https://github.com/nidhaloff/deep-translator) (Google Translate) |
| Production Server | Gunicorn |
| Deployment | Render (via `render.yaml`) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Deepa0912/translator.git
cd translator/english-to-kannada
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### Web App (Flask)

```bash
python app.py
```

Then open your browser at `http://127.0.0.1:5000/`

### Command-Line Translator

```bash
python translator.py
```

Example session:

```
===================================
 English to Kannada Translator
===================================

Enter English text (or type 'exit' to quit): Hello, how are you?

Kannada Translation:
ಹಲೋ, ನೀವು ಹೇಗಿದ್ದೀರಿ?
```

---

## 🔌 API Reference

### `POST /translate`

Translate English text to a target language.

**Request Body (JSON):**

```json
{
  "text": "Hello, how are you?",
  "target": "kn"
}
```

**Response (JSON):**

```json
{
  "success": true,
  "original": "Hello, how are you?",
  "translated": "ಹಲೋ, ನೀವು ಹೇಗಿದ್ದೀರಿ?",
  "target": "kn",
  "target_name": "Kannada"
}
```

**Supported `target` language codes:**

| Code | Language |
|------|----------|
| `kn` | Kannada |
| `hi` | Hindi |
| `ta` | Tamil |
| `te` | Telugu |
| `ml` | Malayalam |
| `bn` | Bengali |
| `mr` | Marathi |
| `gu` | Gujarati |
| `es` | Spanish |
| `fr` | French |
| `de` | German |
| `zh` | Chinese |
| `ar` | Arabic |

---

## 📁 Project Structure

```
translator/
├── english-to-kannada/
│   ├── app.py              # Flask web application & REST API
│   ├── translator.py       # Command-line translation tool
│   ├── translator_html.py  # HTML-based translator variant
│   ├── requirements.txt    # Python dependencies
│   └── templates/
│       └── index.html      # Web UI template
├── api/                    # API module
├── translations.html       # Standalone HTML translation page
├── wsgi.py                 # WSGI entry point for production
├── render.yaml             # Render deployment configuration
├── vercel.json             # Vercel deployment configuration
├── requirements.txt        # Root-level dependencies
└── .gitignore
```

---

## ☁️ Deployment

### Deploy on Render

1. Go to [render.com](https://render.com) and sign in with GitHub
2. Click **New +** → **Web Service**
3. Select this repository — Render auto-detects `render.yaml`
4. Click **Create Web Service**

Your live URL: **[https://language-translator-1waf.onrender.com](https://language-translator-1waf.onrender.com)**

### Deploy on Vercel

A `vercel.json` configuration is also included for deployment on [Vercel](https://vercel.com).

---

## 📦 Dependencies

```
Flask
flask-cors
deep-translator
gunicorn
```

Install all with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/add-new-language`)
3. Commit your changes (`git commit -m 'Add support for Japanese'`)
4. Push to the branch (`git push origin feature/add-new-language`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
