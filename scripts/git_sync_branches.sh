#!/bin/bash
set -euo pipefail

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

# main branch: sync with remote, merge dev, then push
git checkout main
git status
git pull origin main
git merge --ff-only dev
git push origin main

# dev branch: switch back to dev branch
git checkout dev
