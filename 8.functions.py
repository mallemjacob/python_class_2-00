# user-defined functions


# function definition
# def greet(name):  # name = 'cat'
#     # function body
#     if name == 'cat':
#         print('Welcome cat')
#     elif name == 'dog':
#         print('You are not allowed')
#     else:
#         print('Good mornign ' + name)


# # fucntion calling
# greet('cat')  # arugment
# greet('dog')
# greet('mouse')

# Multiple arguments


# def adder(a=0, b=0):
#     print(a + b)


# adder(1, 2)
# adder(10, 20)
# adder()


# def game_name_setter(name='Unknowen User'):
#     print('Welcome ' + name)


# game_name_setter('mouse')

# return  = It returns the value to the calling fuction.

# Default arguments
# def adder(a=0, b=0):
#     return a + b


# output_value1 = adder(1, 2)
# output_value2 = adder(150 + 175)
# output_value3 = adder()


# print(output_value1)
# print(output_value2)
# print(output_value3)

# variable arguments
# def adder(*a):
#     add_result = 0
#     for num in a:
#         add_result = add_result + num

#     return add_result


# print(adder(1, 2, 3, 4, 5))


# Keyword arguments
# def greeter(first_name, last_name):
#     return "Hi " + first_name + " " + last_name


# print(greeter(last_name='cat', first_name='mouse'))


# print('hello', end='')
# print('Bye')


# print('Roll.No', 'Student Name', 'Branch', sep='  |  ')
# print('1', 'Mouse', 'A', sep='  |  ')
# print('2', 'Cat', 'B', sep='  |  ')


# print('hi ' + 'there')
# while True:
#     print('*' * 8, end=' ')

# print(' ' * 3, end='')
# print('********')

import time
space = 0
increaseIndent = True
while True:
    print(' ' * space, end='')
    print('********')
    time.sleep(1)

    if increaseIndent == True:
        space = space + 1
        if space == 10:
            increaseIndent = False
    else:
        space = space - 1
        if space == 0:
            increaseIndent = True

# Zigzag
# ********
#  ********
#   ********
#    ********
#     ********
#      ********
#       ********
#      ********
#     ********
#    ********
#   ********
#  ********
# ********
#  ********
#  ********
#   ********
#    ********
#     ********
#      ********
#       ********
#      ********
#     ********
#    ********
#   ********
#  ********
# ********
