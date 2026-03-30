import subprocess
import platform
import shutil
import time
from pathlib import Path


def open_file_explorer():
    home = str(Path.home())
    system = platform.system()
    if system == "Darwin":  # macOS
        subprocess.run(["open", home])
    elif system == "Windows":
        subprocess.run(["explorer", home])
    else:  # Linux and others
        subprocess.run(["xdg-open", home])


def open_text_file(filename):
    """Open a text file with the system's default text editor."""
    file_path = Path(__file__).parent.parent.parent / "data" / filename
    system = platform.system()
    if system == "Darwin":  # macOS
        subprocess.run(["open", "-a", "TextEdit", file_path])
    elif system == "Windows":
        subprocess.run(["notepad", file_path])
    else:  # Linux and others
        subprocess.run(["xdg-open", file_path])


def close_all_browsers():
    """Close all browser windows (Safari, Chrome, Edge, etc)."""
    system = platform.system()
    if system == "Darwin":  # macOS
        # Close Safari
        subprocess.run(["osascript", "-e", 'tell application "Safari" to quit'], capture_output=True)
        # Close Chrome
        subprocess.run(["osascript", "-e", 'tell application "Google Chrome" to quit'], capture_output=True)
        # Close Edge
        subprocess.run(["osascript", "-e", 'tell application "Microsoft Edge" to quit'], capture_output=True)
        # Close Firefox
        subprocess.run(["osascript", "-e", 'tell application "Firefox" to quit'], capture_output=True)
    elif system == "Windows":
        # Close browsers on Windows
        subprocess.run(["taskkill", "/F", "/IM", "safari.exe"], capture_output=True)
        subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"], capture_output=True)
        subprocess.run(["taskkill", "/F", "/IM", "msedge.exe"], capture_output=True)
        subprocess.run(["taskkill", "/F", "/IM", "firefox.exe"], capture_output=True)
    else:  # Linux and others
        subprocess.run(["pkill", "-f", "safari"], capture_output=True)
        subprocess.run(["pkill", "-f", "chrome"], capture_output=True)
        subprocess.run(["pkill", "-f", "edge"], capture_output=True)
        subprocess.run(["pkill", "-f", "firefox"], capture_output=True)


def prune_dock(keep_file="keep_apps.txt"):
    # Resolve path from this file up to config/ folder
    keep_file_path = Path(__file__).parent.parent.parent / "config" / keep_file
    keep = {line.strip() for line in keep_file_path.read_text().splitlines() if line.strip() and not line.strip().startswith('#')}

    dockutil_path = shutil.which("dockutil")
    if not dockutil_path:
        for candidate in ("/opt/homebrew/bin/dockutil", "/usr/local/bin/dockutil"):
            if Path(candidate).exists():
                dockutil_path = candidate
                break

    if dockutil_path:
        protected = {"Finder", "Trash"}
        killall_path = shutil.which("killall") or "/usr/bin/killall"

        def _list_dock_items() -> list[tuple[str, str | None]]:
            list_result = subprocess.run([dockutil_path, "--list"], capture_output=True, text=True)
            items: list[tuple[str, str | None]] = []
            for line in (list_result.stdout or "").splitlines():
                s = line.strip()
                if not s:
                    continue
                parts = s.split()
                label = parts[0] if parts else ""
                bundle_id = parts[-1] if len(parts) >= 2 else None
                if label:
                    items.append((label, bundle_id))
            return items

        # The Dock can repopulate recent apps asynchronously. Also some apps take time to quit.
        # Retry a few times to converge in a single button press.
        for _ in range(3):
            current_items = _list_dock_items()
            to_remove_from_dock = [(label, bundle_id) for (label, bundle_id) in current_items if label not in keep and label not in protected]
            if not to_remove_from_dock:
                break

            # Quit only the apps we're about to remove from the Dock.
            for label, bundle_id in sorted(to_remove_from_dock, key=lambda x: x[0]):
                if bundle_id:
                    quit_script = f'tell application id "{bundle_id}" to quit'
                else:
                    quit_script = f'tell application "{label}" to quit'
                try:
                    subprocess.run(["osascript", "-e", quit_script], timeout=3, capture_output=True, text=True)
                except subprocess.TimeoutExpired:
                    # Don't crash the Tk callback; proceed to Dock removal.
                    pass

            # Remove Dock items (prefer bundle id).
            for label, bundle_id in sorted(to_remove_from_dock, key=lambda x: x[0]):
                if bundle_id and bundle_id not in keep:
                    subprocess.run([dockutil_path, "--remove", bundle_id, "--no-restart"], capture_output=True, text=True)
                else:
                    subprocess.run([dockutil_path, "--remove", label, "--no-restart"], capture_output=True, text=True)

            subprocess.run([killall_path, "Dock"], capture_output=True, text=True)
            time.sleep(1.0)

        return

    # Remove apps from Dock after quitting (UI scripting fallback)
    keep_list = ", ".join([f'"{x}"' for x in sorted(keep | {"Finder", "Trash"})])
    remove_script = f'''
    tell application "System Events"
        tell process "Dock"
            set keepNames to {{{keep_list}}}
            repeat with dockItem in (UI elements of list 1)
                try
                    set itemName to name of dockItem
                    if keepNames does not contain itemName then
                        perform action "AXShowMenu" of dockItem
                        delay 0.2
                        try
                            click menu item "Remove from Dock" of menu 1 of dockItem
                        end try
                    end if
                end try
            end repeat
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", remove_script], timeout=10, capture_output=True, text=True)
