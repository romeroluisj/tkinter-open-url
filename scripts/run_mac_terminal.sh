#!/bin/bash

# How to run zen-panel from macOS Terminal
# =========================================
# IMPORTANT: Always use the project's .venv Python, NOT python3/system Python.
# Using python3 directly will fail with: ModuleNotFoundError: No module named 'tktools'

# --- Option 1: Run directly (works from any folder) ---
/Users/luisromero/Dev/python/tkinter/zen-panel/.venv/bin/python \
    /Users/luisromero/Dev/python/tkinter/zen-panel/main.py

# --- Option 2: Shell alias (recommended — one word from any folder) ---
# Add this line to ~/.zshrc:
#   alias zen-panel="/Users/luisromero/Dev/python/tkinter/zen-panel/.venv/bin/python /Users/luisromero/Dev/python/tkinter/zen-panel/main.py"
# Reload shell:  source ~/.zshrc
# Then run with: zen-panel