# Product Requirements Document (PRD)

## 1. Product overview

### 1.1 Purpose
`zen-panel` is a lightweight desktop launcher built with Tkinter. It provides a simple GUI for opening groups of URLs (defined in a text file) and includes a macOS Dock cleanup feature (“Zen Dock”) that quits and removes non-essential Dock apps based on a keep list.

### 1.2 Primary users
- A single user (you) who wants fast access to commonly used webpages and a one-click way to reduce Dock clutter.

### 1.3 Goals
- Launch a small Tkinter GUI quickly.
- Provide buttons/sections that open curated groups of URLs.
- Provide a reliable macOS Dock cleanup feature that:
  - Keeps only apps listed in `config/keep_apps.txt` pinned in the Dock.
  - Quits/removes everything else currently in the Dock.

### 1.4 Non-goals
- Cross-platform Dock management (Zen Dock is macOS-focused).
- Full packaging/distribution as a GUI installer (optional in future).

---

## 2. Functional requirements

### 2.1 URL launcher
- The GUI must render sections of buttons (e.g., Default, Code, Languages, etc.).
- Clicking a button must open the corresponding URL group from `data/url_list.txt`.
- Opening URLs should be done via the default browser.

### 2.2 File explorer shortcut
- The “Test” action must open the file explorer for the current directory.

### 2.3 Zen Dock (macOS)
- The “Zen Dock” button must:
  - Read a keep list from `config/keep_apps.txt`.
  - Quit apps that are going to be removed from Dock.
  - Remove Dock items not in the keep list.
  - Never remove `Trash` or `Finder` (system-protected).
- Zen Dock must be reliable for both `persistentApps` and `recentApps` Dock entries.

---

## 3. Data and configuration

### 3.1 URL groups
- File: `data/url_list.txt`
- Format: Python-literal dictionary mapping a button label (key) to a list of URLs (value).

### 3.2 Dock keep list
- File: `config/keep_apps.txt`
- One application name per line.
- Lines starting with `#` are comments.

---

## 4. System requirements

### 4.1 Python
- Python must be built/installed with a compatible Tcl/Tk for Tkinter.
- On macOS, prefer using `pyenv` + Homebrew `tcl-tk` (to avoid Tk version mismatches).

### 4.2 macOS permissions (Zen Dock)
- Zen Dock uses Apple Events (`osascript`) and may require macOS permissions.
- If prompted, allow the relevant app (Terminal / IDE) to control System Events / accessibility.

### 4.3 Homebrew dependency (macOS)
- `dockutil` is required for reliable Dock manipulation:
  - Install: `brew install dockutil`

---

## 5. Runtime dependencies

### 5.1 pip dependencies
- Install via `pip install -r requirements.txt`

### 5.2 System dependencies
- macOS: `dockutil`, Tk-enabled Python.

---

## 6. How to run

### 6.1 Run from terminal
From the repo root:

```bash
python main.py
```

### 6.2 Run from IDE
- Ensure the IDE uses the same Python interpreter that has working Tk.

---

## 7. Reliability and UX requirements
- Zen Dock should converge in a single button press.
- GUI should remain responsive; long operations should be bounded.

---

## 8. Troubleshooting

### 8.1 Tkinter macOS version abort
- Symptom: `macOS XX ... required ... abort`
- Fix: use a Tk-compatible Python build (pyenv + Homebrew `tcl-tk`).

### 8.2 Zen Dock not removing some apps
- Ensure `dockutil` is installed and discoverable.
- Ensure macOS permissions are granted for Apple Events.
