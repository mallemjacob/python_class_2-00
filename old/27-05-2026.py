# Lists


# ------------ 0,  1,  2,  3,  4,   5,  6
number_list = [10, 20, 30, 40, 50, 60, 70]


# Read
print(number_list)

print(number_list[0])

print(number_list[3])

print(number_list[4])


last_index = len(number_list) - 1  # 6


print(number_list[last_index])


# print(number_list[20]) produces index error.

greet = 'hi '

greet = greet + 'there'

print(greet)

# List concatenation
number_list = number_list + [80]

print(number_list)

# Update

# num = 10
# print(num)

# num = 20

# print(num)

number_list = [10, 20, 30, 40, 50, 60, 70]

print(number_list[0])

number_list[0] = 5

print(number_list)
