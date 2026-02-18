"""Flask application package."""

from flask import Flask

from app.routes import main_bp
from app.api import api_bp


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    return app


app = create_app()
