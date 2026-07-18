# 'hi' + 'there'

# "hi" + "there"

# # Doc strings
# '''hi'''

# """hi"""

# # Using quotes in a string
# print("Hi it's my book")
# print('Hi it"s my book')

# # Using escape characters
# print('Hi it\'s my book')
# print("Hi it\"s my book")


# print('This is\t\t my book')

# print('This is another\n\t python code')

# print('this is a windows path \\')


# # Raw Strings

# print(r'This is\n a string')


# # Indexing and Slicing Strings

# '''
# Hello
# 01234
# '''

# for i in 'hello':
#     print(i)


# # The in and not in Operators with Strings

# print('cat' in ['dog', 'cat'])
# print('h' in 'hello')

# print('rat' not in ['dog', 'cat'])
# print('h' not in 'hello')


# fname = 'valkyrie'
# lname = 'loki'
# age = 23

# print('I am ' + fname + ' ' + lname + ' I am ' + str(age))

# # # f-strings
# print(f'I am {fname} {lname} I am {age}. I will be {age + 1} in a year.')


# # String Methods

# name = 'MoUse'
# print(name)
# print(name.upper())
# print(name.lower())
# print(name.title())

# # 'mouse' == 'MoUSe'

# print('Enter you usename:')
# # uname = input()  # MoUSe

# # if uname.lower() == 'mouse':
# #     print('Welcome')


# # isupper(), and islower()

# name = 'mouse'
# print(name.islower())
# print(name.isupper())


# # isalpha()

# name = 'mouse123'

# print(name.isalpha())

# print(name.isalnum())


# good_password_list = []

# password = input('Enter a password. Must contains letter and numbers: ')

# if password.isalnum():
#     good_password_list.append(password)
# else:
#     print('Password is bad')

# print(good_password_list)


# nums = '12345a'

# print(nums.isdecimal())

# # isspace()

# name = '      '
# print(name.isspace())


# name = 'mouse'
# print(name.istitle())


# while True:
#     print('Enter your age: ')
#     age = input()  # '123'
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')


# while True:
#     print("Enter your password: ")
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')


# The startswith() and endswith() Methods

# print('hello'.startswith('h'))
# print('hello'.startswith('o'))
# print('hello'.startswith('h'))
# print('hello'.endswith('o'))


# The join() and split() Methods

# print(','.join(['cat', 'rat', 'bat']))
# print('|'.join(['cat', 'rat', 'bat']))

# print(' --- '.join(['S.no', 'Name', 'Address']))
# print('   --- '.join(['01', 'lyy', '001']))
# print('   --- '.join(['02', 'Val', '101']))
# print('   --- '.join(['03', 'Kye', '100']))
# print('   --- '.join(['04', 'Loki', '000']))


# Split()

# print('My name is Loki'.split(' '))
# print('My name is Loki'.split('a'))


# spam = '''Dear Alice,
# How have you been? I am fine.
# There is a container in the fridge
# that is labeled "Milk Experiment."
# Please do not drink it.
# Sincerely,
# Bob'''

# print(spam.split('\n'))


# Justifying Text with the rjust(), ljust(), and center() Methods

# spam = 'Hello'
# print(spam.rjust(10))
# print(spam.ljust(10))
# print(spam.center(10))


# Removing Whitespace with the strip(), rstrip(), and lstrip() Methods
'admin' == '  admin  '
