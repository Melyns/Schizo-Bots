#!/bin/bash

if [ ! -f "app.py" ]; then
    echo "app.py not found in the current directory."
    exit 1
fi

echo "Starting the FastAPI server. Please close the terminal to stop this server."
uvicorn app:app --host 127.0.0.1 --port 8000 --log-level info &

while true; do
    sleep 5
done
