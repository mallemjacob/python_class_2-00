# items = ['a', 'b', 'c', 'd', 'a']

# print(items)


# my_nums = {1, 2, 3, 4, 5, 5}

# print(my_nums)


# fruits = {"apple", "banana", "cherry", "banana"}

# print(fruits)


# numbers = [1, 2, 3, 4]
# doubled_numbers = []

# for x in numbers:
#     if x % 2 == 0:
#         doubled_numbers.append(x * 2)

# print(doubled_numbers)


numbers = [1, 2, 3, 4]
doubled_numbers = [x * 2 for x in numbers]
doubled_even_numbers = [x * 2 for x in numbers if x % 2 == 0]

print(doubled_numbers)
print(doubled_even_numbers)


vowels = ['a', 'e', 'i', 'o', 'u']

for i in vowels:
    print(i)


vowel_set = {x*2 for x in vowels}

print(vowel_set)
