@echo off
setlocal

if not exist "app.py" (
    echo app.py not found in the current directory.
    exit /b 1
)

echo Starting the FastAPI server. Please close the terminal to stop this server.
start "" /b uvicorn app:app --host 127.0.0.1 --port 8000 --log-level info

:wait
timeout /t 5 >nul
goto wait

endlocal
