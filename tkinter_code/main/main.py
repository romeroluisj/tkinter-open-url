import tkinter as tk
from tkinter_code.tk.window import Window
from tkinter_code.tk.frame import Frame
from tkinter_code.tk.labelframe import LabelFrame
from tkinter_code.tk.label import Label
from tkinter_code.tk.button import Button


def main():
    main_window_title = "Main Window"
    main_window = Window(main_window_title)

    labelframe_00 = LabelFrame(main_window, 0, 0)
    Label(labelframe_00, 0, 0)
    Label(labelframe_00, 1, 1)

    labelframe_11 = LabelFrame(main_window, 1, 1)
    Label(labelframe_11, 0, 0, "any")
    Label(labelframe_11, 1, 1)
    Label(labelframe_11, 0, 1)

    frame_22 = Frame(main_window, 2, 2)
    Button(frame_22, 0, 0, "any", lambda: print("yay"))
    Button(frame_22, 1, 1)

    main_window.start()


# https://www.freecodecamp.org/news/if-name-main-python-example/
if __name__ == '__main__':
    main()
