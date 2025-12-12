#!/bin/bash

# Exit immediately on any error
set -e

# -------------------------------
# 1. Activate virtual environment
# -------------------------------
# Adjust this path if your venv folder has a different name.
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "ERROR: Virtual environment 'venv' not found!"
    exit 1
fi

# -------------------------------
# 2. Run the test suite
# -------------------------------
echo "Running test suite with pytest..."
pytest

TEST_EXIT_CODE=$?

# -------------------------------
# 3. Exit with CI-friendly code
# -------------------------------
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed successfully."
    exit 0
else
    echo "Some tests FAILED."
    exit 1
fi
