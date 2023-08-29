import tkinter as tk


# https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/
class Window(tk.Tk):

    def __init__(self, title="Window Title", geometry="500x500"):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)

    def build(self):
        print(self.title())

    def start(self):
        self.mainloop()


"""
# without inheritance from tk.Tk
class Window:

    def __init__(self, title="Window Title", geometry="500x500"):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.lift()
        self.window.attributes("-topmost", True)
        self.window.after_idle(self.window.attributes, "-topmost", False)

    def start(self):
        self.window.mainloop()
"""
