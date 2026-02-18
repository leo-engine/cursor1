# Plan for this repo

## Current state

- **hello.py** – Simple Hello World script (run with `python3 hello.py`).
- **app/** – Flask app package with `routes`, `templates`, `static`; run with `python3 app.py`.
- **wsgi.py** – WSGI entry point for production (e.g. Gunicorn: `gunicorn wsgi:application`).
- **requirements.txt** – Lists Flask (and its dependencies) for the web app.

## Possible next steps

1. **Expand the Flask app**
   - Add more routes (e.g. `/about`, `/api/health`).
   - Use templates (Jinja2) instead of inline HTML.
   - Add static files (CSS/JS).

2. **Structure** ✓
   - Move the app into a package (e.g. `app/`) with `routes`, `templates`, `static`.
   - Add a proper WSGI entry point for production (e.g. `wsgi.py`).

3. **Quality & deployment**
   - Add tests (e.g. pytest + pytest-flask).
   - Add a `.env` for config and document how to run (e.g. in a README).
   - Add a simple Dockerfile or deployment notes.

4. **Features** (pick what fits)
   - Simple REST API (e.g. CRUD for one resource).
   - Database (SQLite + SQLAlchemy or similar).
   - Basic auth or API keys if needed.

## Suggested order

1. Add a README with run instructions.
2. Introduce templates and 1–2 extra routes.
3. Add tests for the Flask app.
4. Add deployment or Docker if you plan to run it elsewhere.

You can treat this as a living plan: update `PLAN.md` as you add or drop items.
