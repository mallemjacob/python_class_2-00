"""Lesson 8: user-defined functions and return values."""


def greet(name):
    if name == 'cat':
        return 'Welcome cat'
    if name == 'dog':
        return 'You are not allowed'
    return 'Good morning ' + name


def add_numbers(a=0, b=0):
    return a + b


def add_many_numbers(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


def full_name(first_name, last_name):
    return first_name + ' ' + last_name


print(greet('cat'))
print(greet('dog'))
print(greet('mouse'))
print(add_numbers(1, 2))
print(add_numbers())
print(add_many_numbers(1, 2, 3, 4, 5))
print(full_name(last_name='cat', first_name='mouse'))
