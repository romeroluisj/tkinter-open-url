import tkinter as tk


class LabelFrame(tk.LabelFrame):

    def __init__(self, window, row=1, column=1):
        super().__init__(window)
        self.config(text="labelframe")
        self.grid(row=row, column=column)
        tk.Label(self, text="test labelframe").grid(row=0, column=0)
        tk.Label(self, text="test labelframe").grid(row=1, column=0)
        tk.Label(self, text="test labelframe").grid(row=0, column=1)
        tk.Label(self, text="test labelframe").grid(row=1, column=1)
