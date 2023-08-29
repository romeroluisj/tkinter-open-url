import tkinter as tk


class Frame(tk.Frame):

    # Frames cannot have titles
    # bd = shorthand for borderwidth; need bd > 0 for visible border
    # relief = flat (default), raised, sunken, groove, ridge

    def __init__(self, window, row=0, column=0, relief=None, bd=None):
        super().__init__(window, relief=relief, bd=bd)
        self.grid(row=row, column=column)


"""
Ref:
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/frame.html
relief: default = tk.FLAT
bd: default = 0
"""
