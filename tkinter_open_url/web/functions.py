import webbrowser


def open_tabs(button_name=None):
    urls = [
        'https://chat.openai.com',
        'https://www.inquirer.com',
        'https://www.nytimes.com',
        'https://www.elpais.com',
        'https://www.elcomercio.pe'
    ]
    if button_name is not None:
        print("testing01")
    for url in urls:
        webbrowser.open_new_tab(url)
