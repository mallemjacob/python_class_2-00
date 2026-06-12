'''
Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that
keeps calling collatz() on that number until the function returns the value 1.
'''


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


print('Enter a number')
user_value = int(input())  # 25

while True:
    if user_value == 1:  # 3 == 1
        break
    else:
        user_value = collatz(user_value)
