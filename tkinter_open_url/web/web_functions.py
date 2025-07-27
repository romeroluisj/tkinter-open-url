import ast
import os
import webbrowser
import platform
import subprocess
from pathlib import Path


def open_file_explorer():
    system = platform.system()
    if system == "Darwin":  # macOS
        subprocess.run(["open", "."])
    elif system == "Windows":
        subprocess.run(["explorer", "."])
    else:  # Linux and others
        subprocess.run(["xdg-open", "."])


def open_tabs(button_name=None):
    if button_name == "Test":
        open_file_explorer()
        return
    
    urls = get_url_list(button_name)
    for url in urls:
        webbrowser.open_new_tab(url)


def get_url_list(button_name=None):
    print("Current Working Directory:", os.getcwd())  # For debugging

    # Reason: Use absolute path based on this file's location to be robust to working directory
    current_file_dir = Path(__file__).parent
    filename = current_file_dir / "url_list.txt"
    lines = read_lines(filename)

    # Reason: Handle case where file read failed
    if isinstance(lines, str):  # Error message returned
        print(f"Error reading file: {lines}")
        return ['https://www.google.com/']

    # Split every line into "key, value_str"
    for line in lines:
        line = line.strip()  # remove trailing whitespace, newline
        
        # Reason: Skip empty lines and lines without colon separator
        if not line or ':' not in line:
            continue
            
        try:
            key, value_str = line.split(":", 1)
        except ValueError:
            # Reason: Skip malformed lines that can't be split properly
            print(f"Skipping malformed line: {line}")
            continue

        # When key = button_name, convert value_str to actual list
        if key == button_name:
            try:
                url_list = ast.literal_eval(value_str)
                return url_list
            except (ValueError, SyntaxError) as e:
                # Reason: Handle malformed URL list data
                print(f"Error parsing URL list for {button_name}: {e}")
                return ['https://www.google.com/']

    # If for-loop finishes, and button_name is not found in keys
    print("button_name not found in keys")
    url_list = ['https://www.google.com/']
    return url_list


def read_lines(filename):
    """Read lines from a file, handling various error conditions.
    
    Args:
        filename: Path to the file to read (can be string or Path object)
        
    Returns:
        list: List of lines from the file, or error message string if failed
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print("except FileNotFoundError")
        return f"{filename} not found"
    except PermissionError:
        print("except PermissionError")
        return f"Permission denied reading {filename}"
    except Exception as e:
        print(f"Unexpected error reading {filename}: {e}")
        return f"Error reading {filename}: {e}"
