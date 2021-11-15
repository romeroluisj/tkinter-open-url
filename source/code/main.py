from source.tk.window import Window
from source.tk.frame import Frame
from source.tk.labelframe import LabelFrame


def main():
    main_window = Window("Main Window")
    frame_00 = Frame(main_window)
    labelframe_00 = LabelFrame(main_window)
    main_window.start()


# https://www.freecodecamp.org/news/if-name-main-python-example/
if __name__ == '__main__':
    main()
