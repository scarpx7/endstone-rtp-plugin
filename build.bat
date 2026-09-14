@echo off
REM Скрипт для сборки wheel на Windows

echo ======================================
echo Endstone RTP Plugin - Wheel Builder
echo ======================================
echo.

REM Проверка Python
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found in PATH!
    exit /b 1
)
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✓ Python %PYTHON_VERSION% found
echo.

REM Установка зависимостей
echo [2/5] Installing build dependencies...
python -m pip install --upgrade pip wheel setuptools -q
echo ✓ Build dependencies installed
echo.

REM Очистка старых билдов
echo [3/5] Cleaning old builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.egg-info rmdir /s /q *.egg-info
echo ✓ Old builds removed
echo.

REM Сборка wheel
echo [4/5] Building wheel distribution...
python setup.py bdist_wheel >nul 2>&1
echo ✓ Wheel built successfully
echo.

REM Вывод результатов
echo [5/5] Build results:
echo.
if exist dist (
    echo Generated files:
    dir /b dist
    echo.
    echo Installation command:
    echo   pip install dist\endstone_rtp_plugin-*.whl
    echo.
    echo ======================================
    echo ✓ Build completed successfully!
    echo ======================================
) else (
    echo ✗ Build failed: dist directory not found
    exit /b 1
)

pause
