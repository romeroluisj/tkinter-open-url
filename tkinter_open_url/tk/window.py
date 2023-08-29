import tkinter as tk
from tkinter_open_url.tk.button import Button
from tkinter_open_url.tk.labelframe import LabelFrame
from tkinter_open_url.web.functions import open_tabs


class Window(tk.Tk):

    def __init__(self, title="Window Title", geometry="500x500"):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)

    def build(self):
        print(self.title())
        labelframe_00 = LabelFrame(self, 0, 0, "URL buttons")
        Button(labelframe_00, 0, 0, "ChatGPT", command=open_tabs)

    def start(self):
        self.mainloop()
