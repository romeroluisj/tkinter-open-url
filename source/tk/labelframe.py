import tkinter as tk


class LabelFrame(tk.LabelFrame):

    def __init__(self, window, row=1, column=1, text="lf"):
        super().__init__(window, text=text)
        if text == "lf":
            self.config(text=f"{text}_{row}{column}")
        self.grid(row=row, column=column)
