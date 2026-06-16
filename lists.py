# fruits lists
# 1. apples
# 2. babanas
# 3. oranges

# fruit1 = "apples"
# fruit2 = "babanas"
# fruit3 = "oranges"

# Index          0          1           2         3           4             5
fruits_list = ['apples', 'bananas', 'oranges',
               'grapes', 'strawberries', 'kiwi', 'mouse']


# Total items in fruits_list = 3
# last index of the fruits_list = total items - 1

print(fruits_list)

print(fruits_list[0])
print(fruits_list[1])
print(fruits_list[2])
print(fruits_list[3])


print(fruits_list[4])


print(fruits_list[len(fruits_list) - 1])  # 7 - 1

fruits_list = ['apples', 'bananas', 'oranges']

# Read a value from list
print(fruits_list[0])


# Update a value from a list
fruits_list[0] = 'pears'
print(fruits_list)


# Add new items to the list (list concatenation)
fruits_list = fruits_list + ['kiwis']
fruits_list = fruits_list + ['strawberries']
print(fruits_list)


# Creating a new empty list
animals = []
print(animals)

animals = animals + ['cat']  # ['cat']
print(animals)

animals = animals + ['dog']
print(animals)


# Delete an item from the list
print(fruits_list)
del fruits_list[0]

print(fruits_list)


# Accessing last item from the list
# Index           0         1           2
fruits_list = ['apples', 'bananas', 'oranges']
# # reverse        -3         -2          -1


# -3, -2, -1, 0, 1, 2, 3...

print(fruits_list)
print(fruits_list[2])
print(fruits_list[len(fruits_list) - 1])  # important
print(fruits_list[-1])

print(fruits_list[-2])
print(fruits_list[-3])

# String concatenation
print('hi' + 'there')

a = 9
a = a + 1  # a = 10
print(a)
a = a + 1  # 11
print(a)


# String index

name = 'mouse'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
