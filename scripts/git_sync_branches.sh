#!/bin/bash
set -e  # Exit on any error

# Update remote refs
git fetch --all

# Ensure clean working tree
if ! git diff-index --quiet HEAD --; then
    echo "Error: Working tree is dirty. Commit or stash changes first."
    exit 1
fi

# dev branch: push local to remote
git checkout dev
git status
git pull origin dev
git push origin dev

# merge dev branch into main branch
git checkout main
git status
git merge --ff-only dev

# main branch: push local to remote
git status
git pull origin main
git push origin main

# dev branch: switch back to dev branch
git checkout dev
