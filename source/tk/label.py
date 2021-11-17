import tkinter as tk


class Label(tk.Label):

    def __init__(self, frame, row=0, column=0, text="label", relief=tk.GROOVE, bd=1):
        super().__init__(frame, text=text, relief=relief, bd=bd)
        if text == "label":
            self.config(text=f"{text}_{row}{column}")
        self.grid(row=row, column=column)
