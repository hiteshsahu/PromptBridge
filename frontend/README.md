# PromptBridge

PromptBridge is a simple AI prompt application built with **React + Vite + Material UI** on the frontend and a **Python FastAPI** backend that connects securely to the OpenAI API.

The OpenAI API key stays in the backend, so it is never exposed in the browser.

## Tech Stack

### Frontend

- React
- Vite
- Material UI
- JavaScript

### Backend

- Python
- FastAPI
- OpenAI Python SDK
- python-dotenv
- pytest

## Project Structure

```text
Jarvis/
├── backend/
│   ├── .env
│   ├── requirements.txt
│   ├── pyproject.toml
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── openai_connector.py
│   └── tests/
│       ├── __init__.py
│       ├── test_openai_connector.py
│       └── test_openai_connector_integration.py
│
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── App.jsx
│       ├── App.css
│       └── main.jsx
│
├── .gitignore
└── README.md