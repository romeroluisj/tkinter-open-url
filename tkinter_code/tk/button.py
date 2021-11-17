import tkinter as tk


class Button(tk.Button):
    # tk.Button's text not visible on Mac Dark Mode; other option: use ttk.Button
    def __init__(self, frame, row=0, column=0, text="button", command="", relief=tk.RAISED, bd=2):
        super().__init__(frame, text=text, command=command, relief=relief, bd=bd)
        if text == "button":
            self.config(text=f"{text}_{row}{column}")
        self.grid(row=row, column=column)
