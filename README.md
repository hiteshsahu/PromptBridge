# PromptBridge ⛩️

> Open AI Python general purpose assistant


## ⚙️  Installation'
- Install [Python 3.10+](https://www.python.org/downloads/)
- Install [pip](https://pip.pypa.io/en/stable/installation/)

```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build

```

## ▶️ Developer Setup

🔑 Add [OpenAI API key](https://platform.openai.com/settings/organization/api-keys) to `.env` file as environment variables

### Dependencies

Install dependencies from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Don’t forget to freeze the new dependencies if you add any:

```bash
python -m pip freeze > requirements.txt

```

Run the application:

```bash
python -m src.main
```

----

## 🧪 Run Tests

```bash
  # Run Tests
  python -m pytest

  # Run tests with coverage
  python -m pytest --cov=src
  
  # With HTMl Report
  python -m pytest --cov=src --cov-report=html
  
  # Run Only Unit Tests
  python -m pytest -m "not integration"
  
  # Run Only Integration Tests
  python -m pytest -m "integration"

```

