#!/bin/bash
set -e

# Upgrade pip to avoid old versions
python -m pip install --upgrade pip

# Install dependencies globally inside the container
pip install -r requirements.txt

# Optional: Set up PowerShell profile only if needed
PROFILE="/home/vscode/.config/powershell/Microsoft.PowerShell_profile.ps1"
mkdir -p "$(dirname "$PROFILE")"
touch "$PROFILE"

