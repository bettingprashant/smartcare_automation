@echo off
echo ========================================
echo Running Selenium Test Cases with Pytest
echo ========================================

REM Optional: Activate virtual environment
REM call .venv\Scripts\activate

cd /d %~dp0

REM Use python -m pytest to ensure it runs even if PATH is misconfigured
python -m pytest test_cases --maxfail=1 --disable-warnings -v

pause
