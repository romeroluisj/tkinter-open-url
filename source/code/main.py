from source.tk.window import Window
from source.tk.frame import Frame
from source.tk.labelframe import LabelFrame
from source.tk.label import Label
import tkinter as tk


def main():
    main_window = Window("Main Window")

    frame_00 = Frame(main_window, 0, 0)
    Label(frame_00, 0, 0)
    Label(frame_00, 1, 1)

    labelframe_11 = LabelFrame(main_window, 1, 1, "label")
    Label(labelframe_11, 0, 0)
    Label(labelframe_11, 1, 1)
    Label(labelframe_11, 2, 2)

    main_window.start()


# https://www.freecodecamp.org/news/if-name-main-python-example/
if __name__ == '__main__':
    main()
