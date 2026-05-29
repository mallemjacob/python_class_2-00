# loops

# 1. while loop
# 2. for loop

# if condition:
#     codeblock

# indentation

# while condition:
#     codeblock

# codeblock

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

# It asks for age, enter it from your keyboard
student_age = int(input())  # int('21') -> 21

adult_age = 18

if student_age > adult_age:  # 21 > 18
    while True:
        print('Enter you name:')
        name = input()  # 'mouse' -> name = 'mouse'
        if name == 'mouse':  # mouse == mouse
            print('Welcome ' + name)
            for i in range(3):  # 0
                # This loop runs only 3 times
                print('Enter your password: ')
                password = input()  # swordfish
                if password == 'swordfish':
                    print('Welcome to your account.')
                    break
                else:
                    print('Wrong password.')
            # This only executes after completing the for loop
            break
        else:
            print('You are not mouse. Try again')

else:
    print('You are not eligible')


# ask for age
# if age above 18
#   then i will ask for username
#       if username is mouse
#           then i will ask for password
# if password is swordfish
# then i will greet with "Welcome to your account."
# if age is not above 18, You will be given "you are not eligible" warning.


# for loop
# runs a specific number of times.

# while loop
# runs as long as the condition is True.

# while condition:
#     code

# break
# exits out of loop early.

# continue
# skip a loop

# for number in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     if number >= 4 and number <= 6:
#         continue
#     else:
#         print(number) #
#         continue
#         print('welcome')
