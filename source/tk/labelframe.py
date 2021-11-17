import tkinter as tk


class LabelFrame(tk.LabelFrame):

    def __init__(self, window, row=1, column=1, text="lf", relief=tk.GROOVE, bd="2"):
        super().__init__(window, text=text, relief=relief, bd=bd)
        if text == "lf":
            self.config(text=f"{text}_{row}{column}")
        self.grid(row=row, column=column)
