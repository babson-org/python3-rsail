#!/bin/bash
set -e

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv venv
fi

# Upgrade pip inside the venv
echo "Upgrading pip..."
venv/bin/python -m pip install --upgrade pip

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    venv/bin/pip install -r requirements.txt
else
    echo "No requirements.txt found, skipping..."
fi

echo "Setup complete!"

