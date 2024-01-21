@echo off

rem Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b 1
)

rem Check Python version
for /f "tokens=2*" %%i in ('python --version 2^>^&1') do set py_version=%%i

echo Found Python version: %py_version%

rem Check if Python version is at least 3.9
for /f "tokens=1-3 delims=." %%a in ("%py_version%") do (
    set "major_version=%%a"
    set "minor_version=%%b"
    set "patch_version=%%c"
)

if %major_version% lss 3 (
    echo This script requires Python 3 or higher. Please upgrade Python and try again.
    pause
    exit /b 1
) else if %major_version% equ 3 (
    if %minor_version% lss 9 (
        echo This script requires Python 3.9 or higher. Please upgrade Python and try again.
        pause
        exit /b 1
    )
)

rem Run the Python script
python src/main.py

pause
