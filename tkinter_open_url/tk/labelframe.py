import tkinter as tk


class LabelFrame(tk.LabelFrame):

    def __init__(self, window, row=1, column=1, text=None, relief=None, bd=None):
        super().__init__(window, text=text, relief=relief, bd=bd)
        if text == "lf":
            self.config(text=f"{text}_{row}{column}")
        self.grid(row=row, column=column)


"""
Ref:
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/labelframe.html
relief: default = tk.GROOVE
bd: default = 2
"""