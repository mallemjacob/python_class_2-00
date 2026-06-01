# user-defined functions


# function definition
def greet(name):  # name = 'cat'
    # function body
    if name == 'cat':
        print('Welcome cat')
    elif name == 'dog':
        print('You are not allowed')
    else:
        print('Good mornign ' + name)


# fucntion calling
greet('cat')  # arugment
greet('dog')
greet('mouse')
