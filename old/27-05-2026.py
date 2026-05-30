# Lists


# mixed_list = ['car', 'cat', 100, True]


# # ------------ 0,  1,  2,  3,  4,   5,  6
# number_list = [10, 20, 30, 40, 50, 60, 70]


# # Read
# print(number_list)

# print(number_list[0])

# print(number_list[3])

# print(number_list[4])


# last_index = len(number_list) - 1  # 6


# print(number_list[last_index])


# # print(number_list[20]) produces index error.

# greet = 'hi '

# greet = greet + 'there'

# print(greet)

# # List concatenation
# number_list = number_list + [80]

# print(number_list)

# Update

# num = 10
# print(num)

# num = 20

# print(num)

# number_list = [10, 20, 30, 40, 50, 60, 70]

# print(number_list[0])

# number_list[0] = 5

# print(number_list)


# CRUD - Create, Read, Update, Delete

# # Create
# number_list = []
# print(number_list)

# # Update
# number_list = number_list + [10, 20, 30]
# print(number_list)

# # Read
# print(number_list[0])

# # Delete
# del number_list[0]
# print(number_list)


# Create an empty list
# Ask user to enter a number
# chekc if the number is in the list,
# if so, tell him that number already exists
# or else, add the number to the list


# num_list = []

# while True:
#     user_num = int(input('Enter a number: '))
#     if user_num in num_list:
#         print('Duplicate number! Try again')
#     else:
#         num_list = num_list + [user_num]
#         print(num_list)

# Methods

# number_list = [10, 20, 30, 40, 50, 60, 70]

# if 80 in number_list:
#     print(number_list.index(80))
# else:
#     print('80 not in list')

# data types
# intergers
# floats
# strings
# booleans
# lists

# in operator
# Check if a value exists in the list

# index method
# returns the index of a value


number_list = [10, 20, 30, 40, 50, 60, 70]

print(number_list[3])
print(number_list[-4])

print(number_list[::-1])
