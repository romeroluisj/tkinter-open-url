import tkinter as tk


class Frame(tk.Frame):

    def __init__(self, window, row=0, column=0, relief=tk.GROOVE, bd="2"):
        super().__init__(window, relief=relief, bd=bd)
        self.grid(row=row, column=column)
