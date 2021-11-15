import tkinter as tk


class Frame(tk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.config(bd="2", relief=tk.GROOVE)
        self.grid(row=0, column=0)
        tk.Label(self, text="test frame").grid(row=0, column=0)
        tk.Label(self, text="test frame").grid(row=1, column=0)
        tk.Label(self, text="test frame").grid(row=0, column=1)
        tk.Label(self, text="test frame").grid(row=1, column=1)
