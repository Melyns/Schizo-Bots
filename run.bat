@echo off
setlocal

rem Check if app.py exists in the current directory
if not exist "app.py" (
    echo app.py not found in the current directory.
    exit /b 1
)

rem Start the FastAPI server using uvicorn
echo Starting the FastAPI server. Please close the terminal to stop this process.
start "" /b uvicorn app:app --host 127.0.0.1 --port 8000 --log-level info

rem Wait for the user to press Ctrl+C
echo Press Ctrl+C to stop the server.

rem Run an endless loop to keep the batch file running
:wait
timeout /t 5 >nul
goto wait

endlocal
