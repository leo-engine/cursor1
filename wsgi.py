"""WSGI entry point for production servers (e.g. Gunicorn, uWSGI)."""

from app import app

application = app
