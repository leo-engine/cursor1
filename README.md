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

2. Start the server:

   ```bash
   python3 app.py
   ```

3. Open in your browser: **http://127.0.0.1:5000**

To stop the server, press `Ctrl+C` in the terminal.

## Production (WSGI)

Use a WSGI server such as Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 127.0.0.1:5000 wsgi:application
```

## Project layout

- `app.py` – Run the Flask development server
- `wsgi.py` – WSGI entry point for production
- `app/` – Flask application package
  - `app/__init__.py` – App factory
  - `app/routes.py` – Routes (blueprint)
  - `app/templates/` – Jinja2 templates
  - `app/static/` – Static files (CSS, JS)
- `hello.py` – Standalone Hello World script
- `requirements.txt` – Python dependencies (Flask)
- `PLAN.md` – Project plan and next steps
