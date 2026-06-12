"""Lesson 13: handling errors with try and except."""


def divide_ten_by(number):
    try:
        return 10 / number
    except ZeroDivisionError:
        return 'Cannot divide by zero.'
    except TypeError:
        return 'The value must be a number.'


print(divide_ten_by(10))
print(divide_ten_by(5))
print(divide_ten_by(0))
print(divide_ten_by('cat'))


for number in range(1, 21):
    if 10 <= number <= 15:
        continue
    print(number)
