@echo off
title CloudAgent - Multi-Agent Web Dashboard
cls
echo =========================================================================
echo  Starting CloudAgent Multi-Agent Web Dashboard...
echo  Opening browser at http://localhost:8080
echo =========================================================================
echo.
start "" http://localhost:8080
python web_app.py 8080
pause
