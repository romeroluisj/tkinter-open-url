from tkinter_open_url.tk.window import Window
from tkinter_open_url.tk.frame import Frame
from tkinter_open_url.tk.labelframe import LabelFrame
from tkinter_open_url.tk.label import Label
from tkinter_open_url.tk.button import Button
from tkinter_open_url.web.functions import open_tabs


def main():
    main_window_title = "Main Window"
    main_window = Window(main_window_title)

    labelframe_00 = LabelFrame(main_window, 0, 0, "URL buttons")
    Button(labelframe_00, 0, 0, "ChatGPT", command=open_tabs)

    main_window.build()
    main_window.start()


if __name__ == '__main__':
    main()
