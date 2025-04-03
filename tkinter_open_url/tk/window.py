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
        self.build_code_section()
        self.build_financial_section()
        self.build_youtube_section()

    def build_default_section(self):
        row, col = 0, 0
        lf = LabelFrame(self, row, col, "Default")
        button_00 = Button(lf, 0, 0, "Default",
                           command=lambda: open_tabs(button_00.cget('text')))
        button_01 = Button(lf, 0, 1, "Test",
                           command=lambda: open_tabs(button_01.cget('text')))

    def build_code_section(self):
        row, col = 1, 0
        lf = LabelFrame(self, row, col, "Code")
        button_00 = Button(lf, 0, 0, "Code",
                           command=lambda: open_tabs(button_00.cget('text')))
        button_01 = Button(lf, 0, 1, "Courses",
                           command=lambda: open_tabs(button_01.cget('text')))
        button_10 = Button(lf, 1, 0, "AI Chatbots",
                           command=lambda: open_tabs(button_10.cget('text')))
        button_11 = Button(lf, 1, 1, "Azure",
                           command=lambda: open_tabs(button_11.cget('text')))

    def build_financial_section(self):
        row, col = 2, 0
        lf = LabelFrame(self, row, col, "Financial")
        button_00 = Button(lf, 0, 0, "Accounts",
                           command=lambda: open_tabs(button_00.cget('text')))
        button_10 = Button(lf, 1, 0, "Invest",
                           command=lambda: open_tabs(button_10.cget('text')))

    def build_youtube_section(self):
        row, col = 3, 0
        lf = LabelFrame(self, row, col, "YouTube")
        button_00 = Button(lf, 0, 0, "YouTube",
                           command=lambda: open_tabs(button_00.cget('text')))

    def build_language_section(self):
        row, col = 4, 0
        lf = LabelFrame(self, row, col, 'Languages')
        button_00 = Button(lf, 0, 0, 'Deutsch',
                           command=lambda: open_tabs(button_00.cget('text')))
        button_10 = Button(lf, 1, 0, 'Українська',
                           command=lambda: open_tabs(button_10.cget('text')))
        button_20 = Button(lf, 2, 0, 'Русский',
                           command=lambda: open_tabs(button_20.cget('text')))
        button_30 = Button(lf, 3, 0, 'Français',
                           command=lambda: open_tabs(button_30.cget('text')))
        button_40 = Button(lf, 4, 0, 'Italiano',
                           command=lambda: open_tabs(button_40.cget('text')))
        button_50 = Button(lf, 5, 0, 'Português',
                           command=lambda: open_tabs(button_50.cget('text')))
        button_60 = Button(lf, 6, 0, 'Español',
                           command=lambda: open_tabs(button_60.cget('text')))
        button_70 = Button(lf, 7, 0, 'English',
                           command=lambda: open_tabs(button_70.cget('text')))

    def start(self):
        self.mainloop()
