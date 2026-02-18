# Build stage not required for this app; single-stage image.
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application
COPY app/ ./app/
COPY wsgi.py .

# Run with Gunicorn (production WSGI server)
ENV PYTHONUNBUFFERED=1
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:application"]
