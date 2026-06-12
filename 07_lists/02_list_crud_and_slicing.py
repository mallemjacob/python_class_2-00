"""Lesson 15: list CRUD, loops, slicing, and membership."""


fruits_shopping_list = [
    'apples',
    'babanas',
    'grapes',
    'oranges',
    'pears',
    'kiwi',
]

print(fruits_shopping_list[1])
print(fruits_shopping_list[-1])

fruits_shopping_list = fruits_shopping_list + ['mango']
fruits_shopping_list[1] = 'bananas'
del fruits_shopping_list[4]

for index in range(len(fruits_shopping_list)):
    print(str(index) + ' : ' + fruits_shopping_list[index])

print(fruits_shopping_list[0:3])
print(fruits_shopping_list[0:len(fruits_shopping_list)])
print(fruits_shopping_list[:])
print(fruits_shopping_list[1:4])
print(fruits_shopping_list[1:])
print(fruits_shopping_list[::-1])
print(fruits_shopping_list[-2])
print('pears' in fruits_shopping_list)
