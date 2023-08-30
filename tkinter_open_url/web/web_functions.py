import webbrowser


def open_tabs(button_name=None):
    urls = get_url_list(button_name)

    if button_name is not None:
        print(button_name)

    for url in urls:
        webbrowser.open_new_tab(url)


def get_url_list(button_name=None):
    url_list = [
        'https://chat.openai.com',
        'https://weather.com',
        'https://billypenn.com',
        'https://www.inquirer.com',
        'https://www.nytimes.com',
        'https://www.elpais.com',
        'https://www.elcomercio.pe'
    ]
    return url_list
