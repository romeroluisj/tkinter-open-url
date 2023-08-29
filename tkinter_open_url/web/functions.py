import webbrowser


def open_tabs():
    urls = [
        'https://chat.openai.com',
        'https://www.inquirer.com',
        'https://www.nytimes.com',
        'https://www.elpais.com',
        'https://www.elcomercio.pe'
    ]
    print("testing")
    for url in urls:
        webbrowser.open_new_tab(url)
