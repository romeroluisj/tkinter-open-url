import ast
import os
import webbrowser


def open_tabs(button_name=None):
    urls = get_url_list(button_name)

    if button_name is not None:
        print("open_tabs function, button_name = " + button_name)

    for url in urls:
        webbrowser.open_new_tab(url)


def get_url_list(button_name=None):
    print("Current Working Directory:", os.getcwd())  # For debugging

    file_list = os.listdir()

    print("This is the current file list: \n", file_list)

    if button_name is None:
        msg = "get_url_list, button_name is None = empty, no value"
        print(msg)
        return None

    filename = 'url_list.txt'

    # read and print contents of urL_list.txt
    with open(filename, "r") as file:
        content = file.read()
        print("This is the url_list.txt content:\n", content)

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            print("try")
    except FileNotFoundError:
        print("FileNotFoundError")
        return f"{filename} not found in current directory"

    for line in lines:
        line = line.strip()  # remove trailing whitespace, newline
        key, value_str = line.split(":", 1)

        if key == button_name:
            # Convert string representation of list to actual list
            url_list = ast.literal_eval(value_str)
            print(url_list)
            return url_list
        else:
            print("key not found")
