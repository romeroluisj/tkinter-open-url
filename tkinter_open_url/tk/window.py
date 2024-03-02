import tkinter as tk
from tkinter_open_url.tk.button import Button
from tkinter_open_url.tk.labelframe import LabelFrame
from tkinter_open_url.web.web_functions import *


class Window(tk.Tk):

    def __init__(self, title="Window Title", geometry="500x500"):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)

    def build(self):
        # Default section
        self.build_default_section()

        # Other sections
        self.build_language_section()
        self.build_financial_section()
        self.build_youtube_section()

    def build_default_section(self):
        labelframe_00 = LabelFrame(self, 0, 0, "Default")
        button_00 = Button(labelframe_00, 0, 0, "Default",
                           command=lambda: open_tabs(button_00.cget('text')))

    def build_language_section(self):
        labelframe_10 = LabelFrame(self, 1, 0, "Languages")
        button_00 = Button(labelframe_10, 0, 0, "Aid",
                           command=lambda: open_tabs('Language_aid'))
        button_10 = Button(labelframe_10, 1, 0, "English",
                           command=lambda: open_tabs(button_10.cget('text')))
        button_20 = Button(labelframe_10, 2, 0, "Español",
                           command=lambda: open_tabs(button_20.cget('text')))
        button_30 = Button(labelframe_10, 3, 0, "Français",
                           command=lambda: open_tabs(button_30.cget('text')))
        button_40 = Button(labelframe_10, 4, 0, "Deutsch",
                           command=lambda: open_tabs(button_40.cget('text')))
        button_50 = Button(labelframe_10, 5, 0, "Italiano",
                           command=lambda: open_tabs(button_50.cget('text')))

    def build_financial_section(self):
        labelframe_20 = LabelFrame(self, 2, 0, "Financial")
        button_00 = Button(labelframe_20, 0, 0, "Accounts",
                           command=lambda: open_tabs(button_00.cget('text')))
        button_10 = Button(labelframe_20, 1, 0, "Invest",
                           command=lambda: open_tabs(button_10.cget('text')))

    def build_youtube_section(self):
        labelframe_30 = LabelFrame(self, 3, 0, "YouTube")
        button_00 = Button(labelframe_30, 0, 0, "Lisa",
                           command=lambda: open_tabs(button_00.cget('text')))
        button_10 = Button(labelframe_30, 1, 0, "War",
                           command=lambda: open_tabs(button_10.cget('text')))
        button_20 = Button(labelframe_30, 2, 0, "Bachata_TEST",
                           command=lambda: open_tabs(button_20.cget('text')))

    def start(self):
        self.mainloop()
