#!/usr/bin/env python3

import tkinter as tk
import webbrowser
from tkinter_code.tk.window import Window
from tkinter_code.tk.frame import Frame
from tkinter_code.tk.labelframe import LabelFrame
from tkinter_code.tk.label import Label
from tkinter_code.tk.button import Button
from tkinter_code.web.functions import open_tabs

def main():
    main_window_title = "Main Window"
    main_window = Window(main_window_title)

    print_msg = "yay"
    url_chatgpt = "https://chat.openai.com"
    # Labelframes can have titles; place them at window grid's row #, column #
    # Place label(s) at labelframe grid's row #, column #

    labelframe_00 = LabelFrame(main_window, 0, 0, "URL buttons")
    #Button(labelframe_00, 0, 0, "ChatGPT", lambda: webbrowser.open(url_chatgpt))
    Button(labelframe_00, 0, 0, "ChatGPT", command=open_tabs)


    # Frames cannot have titles
    frame_10 = Frame(main_window, 1, 0, "raised", 1)
    Button(frame_10, 0, 0, "any", lambda: print(print_msg))

    main_window.start()


# https://www.freecodecamp.org/news/if-name-main-python-example/
if __name__ == '__main__':
    main()
