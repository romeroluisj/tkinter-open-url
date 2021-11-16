from source.tk.window import Window
from source.tk.frame import Frame
from source.tk.labelframe import LabelFrame
import tkinter as tk


def main():
    main_window = Window("Main Window")

    frame_00 = Frame(main_window, 0, 0)
    tk.Label(frame_00, text="test frame").grid(row=3, column=3)

    labelframe_11 = LabelFrame(main_window, 1, 1)
    tk.Label(labelframe_11, text="test labelframe").grid(row=3, column=3)

    main_window.start()


# https://www.freecodecamp.org/news/if-name-main-python-example/
if __name__ == '__main__':
    main()
