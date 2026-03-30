import tkinter as tk
from tkinter import ttk
from tktools.tk.button import Button
from tktools.tk.labelframe import LabelFrame
from tktools.web.web_functions import *
from tktools.system.system_functions import prune_dock, open_text_file, open_file_explorer  


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
        # System section (to the right of Default)
        self.build_system_section()
        # Do section (to the right of System section)
        self.build_do_section()

        # Other sections
        self.build_dropdown_code_section()
        self.build_dropdown_language_section()
        self.build_financial_section()
        self.build_youtube_section()

    def build_default_section(self):
        row, col = 0, 0
        lf = LabelFrame(self, row, col, "Work")
        button_00 = Button(lf, 0, 0, "Fintech",
                           command=lambda: open_tabs(button_00.cget('text')), width=8)

    def build_system_section(self):
        row, col = 0, 1  # To the right of Work section
        lf = LabelFrame(self, row, col, "System")
        button_00 = Button(lf, 0, 0, "Zen Dock",
                           command=lambda: prune_dock())
        button_01 = Button(lf, 1, 0, "Home dir",
                           command=lambda: open_file_explorer())

    def build_do_section(self):
        row, col = 0, 2  # To the right of System section
        lf = LabelFrame(self, row, col, "Do")
        button_00 = Button(lf, 0, 0, "Macro",
                           command=lambda: open_text_file("macro.txt"))
        button_01 = Button(lf, 1, 0, "Pending",
                           command=lambda: open_text_file("pending.txt"))

    def build_dropdown_code_section(self):
        row, col = 1, 0
        lf = LabelFrame(self, row, col, 'Code')
        
        # Code options (same as buttons)
        code_options = ['Code', 'Courses', 'AI Chatbots', 'Azure']
        
        # Create dropdown
        dropdown = ttk.Combobox(lf, values=code_options, state="readonly", width=8)
        dropdown.grid(row=0, column=0, padx=5, pady=5)
        dropdown.set('Select')  # Default placeholder
        
        # Bind selection event
        def on_code_select(event):
            selected = dropdown.get()
            if selected and selected != 'Select':
                open_tabs(selected)
                # Reset to placeholder after selection
                dropdown.set('Select')
        
        dropdown.bind('<<ComboboxSelected>>', on_code_select)

    def build_financial_section(self):
        row, col = 2, 0
        lf = LabelFrame(self, row, col, "Financial")
        button_00 = Button(lf, 0, 0, "Accounts",
                           command=lambda: open_tabs(button_00.cget('text')), width=8)
        button_10 = Button(lf, 1, 0, "Invest",
                           command=lambda: open_tabs(button_10.cget('text')), width=8)

    def build_youtube_section(self):
        row, col = 3, 0
        lf = LabelFrame(self, row, col, "YouTube")
        button_00 = Button(lf, 0, 0, "YouTube",
                           command=lambda: open_tabs(button_00.cget('text')), width=8)

    def build_dropdown_language_section(self):
        row, col = 4, 0
        lf = LabelFrame(self, row, col, 'Languages')
        
        # Language options (same as buttons)
        languages = ['Deutsch', 'Українська', 'Русский', 'Français', 
                    'Italiano', 'Português', 'Español', 'English']
        
        # Create dropdown
        dropdown = ttk.Combobox(lf, values=languages, state="readonly", width=8)
        dropdown.grid(row=0, column=0, padx=5, pady=5)
        dropdown.set('Select')  # Default placeholder
        
        # Bind selection event
        def on_language_select(event):
            selected = dropdown.get()
            if selected and selected != 'Select':
                open_tabs(selected)
                # Reset to placeholder after selection
                dropdown.set('Select')
        
        dropdown.bind('<<ComboboxSelected>>', on_language_select)

    def start(self):
        self.mainloop()
