# Dictionaries

# nums = ['mouse', 24]

# nums[0]

# mousedict = {'age': 24, 'name': 'mouse', 12345: 'password'}

# # Reading
# print(mousedict['name'])
# print(mousedict['age'])

# # Adding
# mousedict['color'] = 'black'
# print(mousedict['color'])
# print(mousedict)


# print(mousedict.get('location'))

# print(mousedict[12345])


# # Update

# mousedict['age'] = 4
# print(mousedict['age'])


# mousedict.pop('age')

# print(mousedict)


# spam = ['cats', 'dogs', 'moose']
# bacon = ['dogs', 'moose', 'cats']

# print(spam == bacon)


# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# print(eggs == ham)


birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}


while True:

    user_name = input('Enter the user name:')  # 'mouse'
    if user_name == '':
        break
    if user_name in birthdays:
        print(birthdays[user_name])
    else:
        print('That username doesnt exist.')
        birthday = input('Enter the birthday')  # Jan1
        birthdays[user_name] = birthday


print(birthdays)
