from tkinter_open_url.tk.window import Window


def main():
    main_window_title = "Main Window"
    main_window = Window(main_window_title)
    main_window.build()
    main_window.start()


if __name__ == '__main__':
    main()
