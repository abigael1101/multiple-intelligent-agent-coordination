@echo off
title CloudAgent - Push to GitHub
cls
echo =========================================================================
echo   Push CloudAgent Repository to GitHub
echo =========================================================================
echo.
echo 1. Go to https://github.com/new in your browser.
echo 2. Name your repository (e.g., cloud-service-multiagent-system).
echo 3. Leave "Add a README", ".gitignore", and "license" UNCHECKED.
echo 4. Click "Create repository".
echo 5. Copy your repository HTTPS URL.
echo.
echo =========================================================================
echo.

set /p REPO_URL="Paste your GitHub repository URL here (e.g. https://github.com/username/repo.git): "

if "%REPO_URL%"=="" (
    echo.
    echo [ERROR] No URL provided. Aborting.
    pause
    exit /b 1
)

echo.
echo Setting remote origin to: %REPO_URL%
git remote remove origin >nul 2>&1
git remote add origin %REPO_URL%

echo.
echo Pushing branch 'main' to GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo =========================================================================
    echo [SUCCESS] Project successfully pushed to GitHub!
    echo =========================================================================
) else (
    echo.
    echo =========================================================================
    echo [NOTE] If prompted to sign in, complete the browser / token authentication.
    echo =========================================================================
)

echo.
pause
