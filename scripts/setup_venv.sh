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

# Step 2: Install the project in editable mode with all dependencies (runtime + dev/test)
# All dependencies are defined in pyproject.toml (no requirements.txt files needed)
echo "Installing zen-panel with all dependencies..."
.venv/bin/pip install -e ".[dev]"

echo ""
echo "Setup complete. Run the app with:"
echo "  .venv/bin/python main.py"
