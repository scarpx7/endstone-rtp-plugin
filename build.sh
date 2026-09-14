#!/bin/bash

set -e

echo "======================================"
echo "Endstone RTP Plugin - Wheel Builder"
echo "======================================"
echo ""

# Проверка Python
echo "[1/5] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 not found!"
    exit 1
fi
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python $PYTHON_VERSION found"
echo ""

# Установка зависимостей
echo "[2/5] Installing build dependencies..."
python3 -m pip install --upgrade pip wheel setuptools -q
echo "✓ Build dependencies installed"
echo ""

# Очистка старых билдов
echo "[3/5] Cleaning old builds..."
rm -rf build/ dist/ *.egg-info
echo "✓ Old builds removed"
echo ""

# Сборка wheel
echo "[4/5] Building wheel distribution..."
python3 setup.py bdist_wheel > /dev/null 2>&1
echo "✓ Wheel built successfully"
echo ""

# Вывод результатов
echo "[5/5] Build results:"
echo ""
if [ -d "dist" ]; then
    echo "Generated files:"
    ls -lh dist/
    echo ""
    echo "Installation command:"
    echo "  pip install dist/$(ls dist/*.whl)"
    echo ""
    echo "======================================"
    echo "✓ Build completed successfully!"
    echo "======================================"
else
    echo "✗ Build failed: dist/ directory not found"
    exit 1
fi
