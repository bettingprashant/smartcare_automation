@echo off
echo ========================================
echo Running Selenium Test Cases with Pytest
echo ========================================

REM Optional: Activate virtual environment
REM call venv\Scripts\activate

cd /d %~dp0

REM Run all test cases inside test_cases folder using pytest
pytest test_cases --maxfail=1 --disable-warnings -v

pause
