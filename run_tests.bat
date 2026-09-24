@echo off
title CloudAgent - Running Test Suite
cls
echo =========================================================================
echo  Running CloudAgent Automated Test Suite...
echo =========================================================================
echo.
python -m unittest discover -s tests -v
pause
