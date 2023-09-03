import ast
import os
import webbrowser


def open_tabs(button_name=None):
    urls = get_url_list(button_name)
    for url in urls:
        webbrowser.open_new_tab(url)


def get_url_list(button_name=None):
    print("Current Working Directory:", os.getcwd())  # For debugging

    filename = "tkinter_open_url/web/url_list.txt"
    lines = read_lines(filename)

    # Split every line into "key, value_str"
    for line in lines:
        line = line.strip()  # remove trailing whitespace, newline
        key, value_str = line.split(":", 1)

        # When key = button_name, convert value_str to actual list
        if key == button_name:
            url_list = ast.literal_eval(value_str)
            return url_list

    # If for-loop finishes, and button_name is not found in keys
    print("button_name not found in keys")
    url_list = ['https://www.google.com/']
    return url_list


def read_lines(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

    except FileNotFoundError:
        print("except FileNotFoundError")
        return f"{filename} not found in current directory"

    return lines
