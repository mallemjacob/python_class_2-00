# Reuse code with function.

# def greet(greeting):
#     print(greeting)


# greet('good morning')
# greet('good afternoon')
# greet('good evening')


# return statement


# def greet(greeting):
#     return 'Today is ' + greeting


# result = greet('good morning')

# print(result)


# default argument
def adder(a, b, c=0):  # 1, 2
    return a + b + c  # 1 + 2 + 3


print(adder(1, 2, 10))


# keyword arguments
def greet(fname, lname):
    return fname + ' ' + lname


print(greet(lname='cat', fname='mouse'))


# variable arguments

def adder(*nums):
    total = 0
    for num in nums:  # nums = 1,2,3,4,5      num = 5
        total = total + num  # 10 + 5

    return total


print(adder(1, 2, 3, 4, 5))
print(adder(1, 2))
print(adder(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
