def calulator(num):

    try:
        return 10 / num
    except ZeroDivisionError:
        return 10 / 1
    except TypeError:
        print('both valeus muste be same type')
    except SyntaxError:
        print('Check syntax')


print(calulator(10))
print(calulator(5))
print(calulator(0))
print(calulator(2))


'try counting numbers except if it is between 10 and 15 then skip them'
