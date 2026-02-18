"""Pytest configuration and fixtures."""

import pytest

from app import create_app


@pytest.fixture
def app():
    """Create app with testing config."""
    app = create_app()
    app.config["TESTING"] = True
    return app
