import tkinter as tk


class Button(tk.Button):
    # tk.Button's text not visible on Mac Dark Mode; other option: use ttk.Button
    def __init__(self, frame, row=0, column=0, text=None, command=None, relief=None, bd=None):
        super().__init__(frame, text=text, command=command, relief=relief, bd=bd)
        if text is None:
            self.config(text=f"{text}_{row}{column}")
        if command is None:
            self.config(command=lambda: print("Command is not configured"))
        self.grid(row=row, column=column)


"""
Ref:
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/button.html
relief: default = tk.RAISED
bd: default = 2
"""
