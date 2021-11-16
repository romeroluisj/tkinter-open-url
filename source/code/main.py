from source.tk.window import Window
from source.tk.frame import Frame
from source.tk.labelframe import LabelFrame
import tkinter as tk


def main():
    main_window = Window("Main Window")

    frame_00 = Frame(main_window, 0, 0)
    tk.Label(frame_00, text="label_00").grid(row=0, column=0)
    tk.Label(frame_00, text="label_11").grid(row=1, column=1)

    labelframe_11 = LabelFrame(main_window, 1, 1, "label")
    tk.Label(labelframe_11, text="label_00").grid(row=0, column=0)
    tk.Label(labelframe_11, text="label_11").grid(row=1, column=1)

    # NEXT STEP: create Label class same as Frame/LabelFrame class

    main_window.start()


# https://www.freecodecamp.org/news/if-name-main-python-example/
if __name__ == '__main__':
    main()
