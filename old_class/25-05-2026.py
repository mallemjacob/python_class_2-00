# Functions
# we dont have to duplicate code

# function definition
# def greet(name='nobody', age=0):  # parameters
#     # function body

#     return 'Hi there ' + name + '. You are ' + str(age) + ' years old.'


# # function calling
# print(greet('cat', 5))  # arguments
# print(greet('dog', 11))
# print(greet('bird', 3))

# print(greet())


def left():
    print('going left')


def right():
    print('going right')


def backward():
    print('going back')


def forward():
    print('going straight')


def start_game(name='nobody'):
    score = 0
    print('Game started')
    print('Welcome ' + name)
    print('You score is ' + str(score))
    print('Where do you want to go? ')
    print('r for right, l for left, f for forward, b for back')

    direction = input()


while True:
    print('Welcome to space rangers')
    name = input('Enter your name: ')
    print('Hi ' + name)
    start = input(
        'Do you want to start the game? Type y for yes or n for no: ')
    if start == 'y':
        start_game(name)
    elif start == 'n':
        print('See you again!')
        break
    else:
        print('You must only enter y or n. Not any other chracters.')
