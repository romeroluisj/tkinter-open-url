import tkinter as tk


class Label(tk.Label):

    def __init__(self, frame, row=0, column=0, text=None, relief=None, bd=None):
        super().__init__(frame, text=text, relief=relief, bd=bd)
        if text is None:
            self.config(text=f"{text}_{row}{column}")
        self.grid(row=row, column=column)


"""
Ref:
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/label.html
relief: default = tk.FLAT
bd: default = 2
"""