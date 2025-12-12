#!/bin/bash

set -e

echo "Activating virtual environment..."

if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "❌ No virtual environment found!"
    exit 1
fi

echo "Running tests..."
pytest

if [ $? -eq 0 ]; then
    echo "✅ All tests passed!"
    exit 0
else
    echo "❌ Tests failed!"
    exit 1
fi
