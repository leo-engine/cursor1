# Cursor1

A simple Python project with a Hello World script and a minimal Flask app.

## Prerequisites

- Python 3.8+
- pip

## Run the Hello World script

```bash
python3 hello.py
```

You should see: `Hello, World!`

## Run the Flask app

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Copy env example and adjust:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` to set `FLASK_DEBUG=1` for development. Do not commit `.env`.

3. Start the server:

   ```bash
   python3 app.py
   ```

4. Open in your browser: **http://127.0.0.1:5000**

To stop the server, press `Ctrl+C` in the terminal.

## Tests

```bash
pip install -r requirements-dev.txt
pytest
```

Run with verbose output: `pytest -v`

## Production (WSGI)

Use a WSGI server such as Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 127.0.0.1:5000 wsgi:application
```

## Docker

Build and run:

```bash
docker build -t cursor1 .
docker run -p 5000:5000 cursor1
```

Then open **http://127.0.0.1:5000**.

## Project layout

- `app.py` – Run the Flask development server
- `wsgi.py` – WSGI entry point for production
- `app/` – Flask application package
  - `app/__init__.py` – App factory
  - `app/routes.py` – Routes (blueprint)
  - `app/templates/` – Jinja2 templates
  - `app/static/` – Static files (CSS, JS)
- `hello.py` – Standalone Hello World script
- `requirements.txt` – Python dependencies (Flask, python-dotenv)
- `requirements-dev.txt` – Dev dependencies (pytest, pytest-flask)
- `tests/` – Pytest tests
- `.env.example` – Example env file (copy to `.env`)
- `Dockerfile` – Image for running the app with Gunicorn
- `PLAN.md` – Project plan and next steps
