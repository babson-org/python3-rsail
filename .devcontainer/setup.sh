#!/bin/bash
set -e

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv venv
fi

# Detect shell type
if [ -n "$PSModulePath" ] || [ "$SHELL" = "" ]; then
    # Likely PowerShell
    echo "Detected PowerShell shell..."
    ACTIVATE_SCRIPT="venv\\Scripts\\Activate.ps1"
    if [ -f "$ACTIVATE_SCRIPT" ]; then
        echo "Activating virtual environment in PowerShell..."
        pwsh -Command "& { . .\\$ACTIVATE_SCRIPT }"
    else
        echo "Error: $ACTIVATE_SCRIPT not found"
        exit 1
    fi
else
    # Assume Bash / Linux
    echo "Detected Bash / Linux shell..."
    ACTIVATE_SCRIPT="venv/bin/activate"
    if [ -f "$ACTIVATE_SCRIPT" ]; then
        echo "Activating virtual environment in Bash..."
        source "$ACTIVATE_SCRIPT"
    else
        echo "Error: $ACTIVATE_SCRIPT not found"
        exit 1
    fi
fi

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found, skipping..."
fi

# Optional: set up PowerShell profile in Codespaces / devcontainer
PROFILE="$HOME/.config/powershell/Microsoft.PowerShell_profile.ps1"
mkdir -p "$(dirname "$PROFILE")"
touch "$PROFILE"
if ! grep -q "venv" "$PROFILE"; then
    echo "if (Test-Path venv\\Scripts\\Activate.ps1) { . venv\\Scripts\\Activate.ps1 }" >> "$PROFILE"
fi

echo "Setup complete!"

