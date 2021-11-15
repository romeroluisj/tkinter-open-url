import tkinter as tk


class Frame1(tk.LabelFrame):

    def __init__(self, window):
        super().__init__(window)
        self.config(text="labelframe")
        # self.master.title("Simple")
        self.grid(row=0, column=0)
        tk.Label(self, text="test label").grid()
