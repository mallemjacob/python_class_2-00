# loops

# 1. while loop
# 2. for loop

# if condition:
#     codeblock

# while condition:
#     codeblock


# if True:
#     print('hi')

# while i am in the class, write numbers in your notebook statring from 1 2

# if count is 5 stop the loop

# count = 1

# while count <= 10:  # 5 <= 10
#     if count == 5:  # 5 == 5
#         break
#     else:
#         print(count)  # 4
#         count = count + 1  # 4 + 1 = 5

# print('the end')

# break


print('Enter you age: ')
student_age = int(input())  # int('21') -> 21

adult_age = 18

if student_age > adult_age:  # 21 > 18
    while True:
        print('Enter you name:')
        name = input()  # 'mouse' -> name = 'mouse'
        if name == 'mouse':  # mouse == mouse
            print('Welcome ' + name)
            print('Enter your password: ')
            password = input()  # swordfish
            if password == 'swordfish':
                print('Welcome to your account.')
                break
            else:
                print('Wrong password.')

        else:
            print('You are not mouse. Try again')
else:
    print('You are not eligible')


# ask for age
# if age above 18
# then i will ask for username
# if usetname is mouse
# then i will ask for password
# if password is swordfish
# then i will greet with "Welcome to your account."
