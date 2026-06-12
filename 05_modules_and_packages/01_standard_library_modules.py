"""Lesson 11: importing and using standard library modules."""

import webbrowser


def open_website(website_name):
    url = 'https://www.' + website_name + '.com'
    webbrowser.open(url)
    return url


def main():
    website_name = input('Enter a website name: ')
    opened_url = open_website(website_name)
    print('Opened ' + opened_url)


if __name__ == '__main__':
    main()
