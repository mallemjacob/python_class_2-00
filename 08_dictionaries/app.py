# list
animals1 = ['cat', 'dog', 'mouse', 'rat',]

animals2 = ['dog', 'mouse', 'cat', 'rat',]

# print(animals1 == animals2)  # False

# dictionary
animals_dictionary1 = {
    'my_pet': 'cat',
    'age': 5,
    'loud': True,
    12345: 'code'
}

animals_dictionary2 = {
    12345: 'code',
    'my_pet': 'cat',
    'loud': True,
    'age': 5
}

# print(animals_dictionary1 == animals_dictionary2)  # True


# Accessing a item from dictionary
# print(animals_dictionary1['loud'])

# Update a value in the dictionary
# print(animals_dictionary2)
# animals_dictionary2['age'] = 6
# print(animals_dictionary2)


# lists in dictionary

list_of_users = [
    {
        'name': 'valkyrie',
        'age': 23,
        'langs': ['German', 'French', 'Spanish']
    },

    {
        'name': 'bob',
        'age': 21,
        'langs': ['Thai', 'Latin', 'Spanish']
    }

]

print(list_of_users[0]['langs'][2])


# print(user2)
# print(user2['name'])
# print(user2['age'])
# print(user2['langs'][1])
