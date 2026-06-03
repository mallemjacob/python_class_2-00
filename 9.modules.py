import webbrowser


print('Enter a website name:')
website_name = input()  # facebook

webbrowser.open("https://www." + website_name + ".com")
