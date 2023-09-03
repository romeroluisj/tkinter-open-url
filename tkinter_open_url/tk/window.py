import tkinter as tk
from tkinter_open_url.tk.button import Button
from tkinter_open_url.tk.labelframe import LabelFrame
from tkinter_open_url.web.web_functions import *


class Window(tk.Tk):

    def __init__(self, title="Window Title", geometry="500x500"):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)

    def build(self):
        labelframe_00 = LabelFrame(self, 0, 0, "URL buttons")

        # URL buttons
        button_00 = Button(labelframe_00, 0, 0, "Default",
                           command=lambda: open_tabs(button_00.cget('text')))
        button_10 = Button(labelframe_00, 1, 0, "English",
                           command=lambda: open_tabs(button_10.cget('text')))
        button_20 = Button(labelframe_00, 2, 0, "Español",
                           command=lambda: open_tabs(button_20.cget('text')))

    def start(self):
        self.mainloop()
