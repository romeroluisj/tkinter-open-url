import webbrowser


def open_tabs(button_name=None):
    urls = [
        'https://chat.openai.com',
        'https://weather.com',
        'https://billypenn.com',
        'https://www.inquirer.com',
        'https://www.nytimes.com',
        'https://www.elpais.com',
        'https://www.elcomercio.pe'
    ]
    if button_name is not None:
        print(button_name)

    test_string = get_url_list(button_name)
    print(test_string)

    for url in urls:
        webbrowser.open_new_tab(url)


def get_url_list(button_name=None):
    return button_name + "_testing_url_list"
