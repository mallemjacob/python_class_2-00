# fruits lists
# 1. apples
# 2. babanas
# 3. oranges

# fruit1 = "apples"
# fruit2 = "babanas"
# fruit3 = "oranges"

# Index          0          1           2         3           4             5
# fruits_list = ['apples', 'bananas', 'oranges',
#                'grapes', 'strawberries', 'kiwi', 'mouse']


# # Total items in fruits_list = 3
# # last index of the fruits_list = total items - 1

# print(fruits_list)

# print(fruits_list[0])
# print(fruits_list[1])
# print(fruits_list[2])
# print(fruits_list[3])


# print(fruits_list[4])


# print(fruits_list[len(fruits_list) - 1])  # 7 - 1

# fruits_list = ['apples', 'bananas', 'oranges']

# Read a value from list
print(fruits_list[0])


# # Update a value from a list
fruits_list[0] = 'pears'
print(fruits_list)


# # Add new items to the list (list concatenation)
fruits_list = fruits_list + ['kiwis']
fruits_list = fruits_list + ['strawberries']
print(fruits_list)


# # Creating a new empty list
animals = []
print(animals)

# animals = animals + ['cat']  # ['cat']
# print(animals)

# animals = animals + ['dog']
# print(animals)


# # Delete an item from the list
print(fruits_list)
del fruits_list[0]

# print(fruits_list)


# # Accessing last item from the list
# # Index           0         1           2
fruits_list = ['apples', 'bananas', 'oranges']
# # # reverse     -3         -2          -1


# # -3, -2, -1, 0, 1, 2, 3...

# print(fruits_list)
# print(fruits_list[2])
print(fruits_list[len(fruits_list) - 1])  # very very important
# print(fruits_list[-1])

# print(fruits_list[-2])
# print(fruits_list[-3])

# # String concatenation
# print('hi' + 'there')

# a = 9
# a = a + 1  # a = 10
# print(a)
# a = a + 1  # 11
# print(a)


# # String index

name = 'mouse'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])


# # check if a value exists in a list
fruits_list = ['apples', 'bananas', 'oranges']


print('apples' in fruits_list)  # True
print('kiwi' in fruits_list)  # False

print('kiwi' not in fruits_list)  # True
print('apples' not in fruits_list)  # False

# Find index of an item
print(fruits_list.index('apples'))
print(fruits_list.index('oranges'))

# Functions-  general purpose
# int(), str(), print()

# methods
# [1,2,3].index(2)


item_to_search = 'apples'

if item_to_search in fruits_list:
    print(fruits_list.index(item_to_search))
else:
    print(item_to_search + ' not in list')


# # Slice
fruits_list = ['apples', 'bananas', 'oranges',
               'grapes', 'strawberries', 'kiwi', 'mouse']


print(fruits_list[2:6])


# # reverse a list

print(fruits_list[::-1])


# step value - skips values
print(fruits_list[::1])
print(fruits_list[::2])


# functions
# print(), input(), str(), len(), int()

# List methods

# append() = Adds an element at the end of the list
animals = ['cat', 'dog', 'rat']
print(animals)

animals.append('mouse')

print(animals)

# # clear()	= Removes all the elements from the list
animals.clear()

print(animals)


# # count() = Returns the number of elements with the specified value
animals = ['cat', 'dog', 'rat', 'bug', 'snake', 'dog', 'cat']

print(animals.count('cat'))


# # extend()	= Add the elements of a list (or any iterable), to the end of the current list

a1 = [1, 2, 3]
a2 = [4, 5, 6]

a1.extend(a2)

print(a1)


# # insert() = Adds an element at the specified position

animals.insert(2, 'parrot')

print(animals)


# # pop()	= Removes the element at the specified position

print(animals)

animals.pop()
animals.pop(0)

print(animals)


# # remove()	Removes the first item with the specified value

animals.remove('parrot')
print(animals)


# # reverse()	= Reverses the order of the list

animals.reverse()

print(animals)


# # sort() = Sorts the list

# nums = [1, 3, 2, 5, 4, 9, 8, 7, 6]
# animals = ['ant', 'cat', 'bug', 'elephant', 'dog']

# nums.sort()
# animals.sort()

# print(nums)
# print(animals)


# cat list

cats = []

while True:
    cat_name = input('Enter a cat name:')  # snoopy

    if cat_name == '':
        break
    elif cat_name in cats:
        print('Name already exists. Give a new name')
    else:
        cats.append(cat_name)


print("The cat names are: ")

for name in cats:
    print(name)


# List replication

l = ['a', 'b', 'c']
print(l * 3)


# str to list

name = 'mouse'
name_list = list(name)

print(name_list)
