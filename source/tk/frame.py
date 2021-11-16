import tkinter as tk


class Frame(tk.Frame):

    def __init__(self, window, row=0, column=0):
        super().__init__(window, bd="2", relief=tk.GROOVE)
        self.grid(row=row, column=column)
