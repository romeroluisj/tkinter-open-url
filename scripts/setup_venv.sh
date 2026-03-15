#!/bin/bash
set -euo pipefail

# Run this script once on any new machine after cloning the repo.
# It creates the virtual environment and installs all dependencies.
#
# Usage:
#   ./scripts/setup_venv.sh

# Step 1: Create the virtual environment (skip if it already exists)
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python -m venv .venv
else
    echo ".venv already exists, skipping creation."
fi

# Step 2: Install all dependencies (runtime + dev/test tools)
echo "Installing dependencies..."
.venv/bin/pip install -r requirements-dev.txt

# Step 3: Install the project itself in editable mode
# This makes the tktools package importable from anywhere (e.g. when running pytest)
echo "Installing zen-panel in editable mode..."
.venv/bin/pip install -e .

echo ""
echo "Setup complete. Run the app with:"
echo "  .venv/bin/python main.py"
