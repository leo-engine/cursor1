#!/usr/bin/env python3
"""Run the Flask development server."""

from app import app

if __name__ == "__main__":
    app.run(debug=True)
