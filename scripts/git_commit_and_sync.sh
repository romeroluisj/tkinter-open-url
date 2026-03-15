#!/usr/bin/env bash
set -euo pipefail

# Stage all changes
git status
git add -A
git status

# Commit if there is anything staged
if git diff --cached --quiet; then
  echo "No staged changes to commit."
else
  changed_files=$(git diff --cached --name-only)
  file_count=$(printf "%s\n" "$changed_files" | sed '/^$/d' | wc -l | tr -d ' ')

  if [[ "$file_count" == "1" ]]; then
    default_msg="Update $(printf "%s" "$changed_files" | head -n 1)"
  else
    default_msg="Update ${file_count} files"
  fi

  echo "Suggested commit message: ${default_msg}"
  read -r -p "Commit message [${default_msg}]: " msg
  msg=${msg:-$default_msg}

  git commit -m "$msg"
fi

# Sync/merge branches and push to remotes
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
"${script_dir}/git_sync_branches.sh"
