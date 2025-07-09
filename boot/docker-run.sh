#!/bin/bash

# Activate virtual environment
source /opt/venv/bin/activate

# Go to project directory
cd /code

# Set default values
RUN_PORT=${RUN_PORT:-8000}
RUN_HOST=${RUN_HOST:-0.0.0.0}

# Run FastAPI app with Gunicorn
exec gunicorn -k uvicorn.workers.UvicornWorker -b ${RUN_HOST}:${RUN_PORT} main:app
