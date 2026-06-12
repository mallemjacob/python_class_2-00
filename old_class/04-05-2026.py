# comparison operators
# 2 > 1  # True
# 10 < 5  # False


# boolean datatype - True, False

# boolean operators
# and, or , not

# 2 * 4
# 2 > 1 and 10 < 5


# comparison --> booleans --> boolean operators


# if conditon and condition and condition:
#     block of code
# elif conditon or condition:
#     block of code
# else:
#     block of code


# nested if statements

# if 20 > 10:
#     print('it is true')
#     name = 'mouse'
#     print('Enter your age:')
#     age = int(input())
#     if age > 18:
#         print("you are allowed to drive a car.")
#     else:
#         print('You cannot drive a car.')
# else:
#     print('It is false.')

# if you are above 18, you can drive a car and then you can also ride a bike and if you have a job then you can also rent a house.

# if your username is correct then i will ask you for you password, if you password is also correct then i will give your home page

# if you come to class at 8, then you can take notes and then you can attend the exam and then you can also apply for next exam

# if your age is above 18, then you will be asked for your username, or else you will be warned with 'You should be above 18 years old to login.' If your username is equal to 'mouse' then you will be asked for your password or else you will be warned with 'Wrong username', if you password is equal to 'killer' then you will be greet with 'welcome to your page' or else you will be warned with 'Wrong password'.

print('Enter your age:')
age = int(input())  # 21
if age > 18:
    print('Enter your username')
    username = input()  # mouse
    if username == 'mouse':
        print('Enter you password')
        password = input()  # killer
        if password == 'killer':
            print('welcome to your page!')
        else:
            print('Wrong password')
    else:
        print('Wrong username')
else:
    print('You should be above 18 years old to login.')


# if your age is above 18, then you will be asked for your username, or else you will be warned with 'You should be above 18 years old to login.' If your username is equal to 'mouse' then you will be asked for your password or else you will be warned with 'Wrong username', if you password is equal to 'killer' then you will be greet with 'welcome to your page' or else you will be warned with 'Wrong password'.


# Homework

# At a secure research lab, visitors must pass through multiple verification checkpoints.

# Checkpoint 1 verifies Employee ID
# Checkpoint 2 verifies Access Code
# Checkpoint 3 verifies Clearance Badge

# If a person is above 21 years of age, they are allowed to enter Checkpoint 1 and must provide their Employee ID. If the ID matches "falcon", they proceed to Checkpoint 2; otherwise, they are stopped with the message "Invalid Employee ID".

# At Checkpoint 2, the person must provide their access code. If the code matches "delta42", they proceed to Checkpoint 3; otherwise, they are stopped with the message "Access Denied: Incorrect Code".

# At Checkpoint 3, if all previous checks are cleared, the person is granted full access with the message "Access Granted. Welcome to the lab.".

# If the person is 21 years old or below, they are denied entry with the message: "You must be above 21 years old to enter the facility.".
