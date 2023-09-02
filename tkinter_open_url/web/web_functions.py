import ast
import os
import webbrowser


def open_tabs(button_name=None):
    urls = get_url_list(button_name)

    for url in urls:
        webbrowser.open_new_tab(url)


def get_url_list(button_name=None):
    print("Current Working Directory:", os.getcwd())  # For debugging

    filename = "url_list.txt"
    filename_lines = file_readlines(filename)

    for line in filename_lines:
        line = line.strip()  # remove trailing whitespace, newline
        key, value_str = line.split(":", 1)

        if key == button_name:
            # Convert string representation of list to actual list
            url_list = ast.literal_eval(value_str)
            print("This is the url_list:")
            return url_list

    # If for-loop finishes, and button_name is not found in keys
    print("button_name not found in keys")
    return None


def file_readlines(filename):
    lines = None
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("except FileNotFoundError")
        return f"{filename} not found in current directory"
    return lines