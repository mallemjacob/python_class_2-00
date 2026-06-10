# Lists

# name = 'mouse'
# age = 24

# 'cat', 'bat', 'rat', 'mouse', 'dog'

# # Fruits Shopping list
# 1. apples
# 2. bananas
# 3. grapes
# 4. oranges
# -----------------------  -5        -4         -3        -2       -1
# fruits_shopping_list = ['apples', 'babanas', 'grapes', 'oranges', 'pears']
# ----------------------- 0           1          2          3        4
# print(fruits_shopping_list)


# # CRUD - Create, Read, Update, Delete

# # Reading
# print(fruits_shopping_list[1])
# print(fruits_shopping_list[3])
# print(fruits_shopping_list[len(fruits_shopping_list) - 1])
# print(fruits_shopping_list[-1])

# # Creating

# nums_list = []

# # Update

# nums_list = nums_list + ['cat']
# nums_list = nums_list + ['rat']

# print(nums_list)


# # Delete
# del fruits_shopping_list[4]
# print(fruits_shopping_list)


# for loop

fruits_shopping_list = ['apples', 'babanas',
                        'grapes', 'oranges', 'pears', 'kiwi']

for index in range(len(fruits_shopping_list)):  # 0,1,2,3,4
    print(str(index) + ' : ' + fruits_shopping_list[index])


# sclicing

print(fruits_shopping_list[0:3])
print(fruits_shopping_list[0:len(fruits_shopping_list)])
print(fruits_shopping_list[:])

print(fruits_shopping_list[1:4])
print(fruits_shopping_list[1:])

print(fruits_shopping_list[::-1])


print(fruits_shopping_list[-2])


# Check if an item exists in a list

print('pears' in fruits_shopping_list)
