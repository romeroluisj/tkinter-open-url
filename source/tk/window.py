import tkinter as tk


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Window Title")
        self.window.geometry("500x500")
        self.window.lift()
        self.window.attributes("-topmost", True)
        self.window.after_idle(self.window.attributes, "-topmost", False)

    def start(self):
        self.window.mainloop()
