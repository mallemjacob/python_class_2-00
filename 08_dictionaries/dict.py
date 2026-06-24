# fruits_list = ['bananas', 'oranges', 'apples']

# print(fruits_list[0])

# # //////////////////////

# fruits_dictionary = {
#     'fruit2': 'bananas',
#     'fruit3': 'oranges',
#     'fruit1': 'apples'
# }

# print(fruits_dictionary['fruit1'])

# person1 = {
#     'name': 'mouse',
#     'age': 23,
#     12345: 'passcode',
#     True: 'adult'
# }

# print(person1[12345])
# print(person1[True])


# complex data structues with lists and dictionaries


# person1_details = {
#     'name': 'Tom',
#     'age': 23,
#     'location': 'US',
#     'langs': ['English', 'French', 'German']
# }


# print(person1_details.keys())
# print(person1_details.values())
# print(person1_details.items())


# list_of_users = [
#     {
#         'name': 'Tom',
#         'age': 21,
#         'location': 'US',
#         'langs': ['English', 'French', 'German']
#     },

#     {
#         'name': 'Mouse',
#         'age': 22,
#         'location': 'Germany',
#         'langs': ['English', 'Italian', 'Spanish']
#     },

#     {
#         'name': 'Cat',
#         'age': 23,
#         'location': 'France',
#         'langs': ['English', 'Japanese', 'Korean']
#     }
# ]


# # print(list_of_users[2]['langs'][1])


# for i in list_of_users:
#     print(i['langs'])

# 'Apr 1': 'Julia', "Dec 12": 'Diana'

birthdays = {}


while True:
    birthday = input("Enter a person's birthday: ")  # Apr 1
    if birthday == '':
        break
    elif birthday in birthdays.keys():
        print("It's " + birthdays[birthday] + "'s birthday.")
    else:
        name = input('Enter the person name: ')  # Julia
        birthdays[birthday] = name


for i in birthdays.items():
    print(i)
