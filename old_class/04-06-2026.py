# Multiline Strings with Triple Quotes

''' This is my first string program
    I wrote this in June 2026       '''

# This is my first string program
# I wrote this in June 2026

# print('''I am not land or timber
# nor are you
# ocean or celestial body,

# but rather we are
# the small animals
# we have always been.

# The land and the sea
# know each other
# at the threshold

# where they meet,
# as we know something
# of one another''')


# nums = [1, 2, 3, 4, 5]

# name = 'Hello'

# print(name[0])


while True:
    print('Enter your age:')
    age = input()  # '12'
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()  # pswd123
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
