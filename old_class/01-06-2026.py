# List methods

# mylist = [1, 2, 2, 2, 2, 3, 4, 5]

# print(mylist)

# mylist.append(6)
# print(mylist)

# # mylist.clear()

# # print(mylist)

# # newlist = mylist.copy()

# # print(newlist)

# print(mylist.count(2))

# mylist.extend(['a', 'b'])

# print(mylist)

# mylist.insert(0, 'start')
# mylist.insert(5, 'middle')
# print(mylist)

# mylist.pop()
# mylist.remove('a')

# mylist.reverse()


# nums = [5, 2, 7, 0, 1, 2, 4, 5]

# nums.sort()

# print(nums)


# # iterable types
# # 1. list
# # 2. string

# for num in nums:
#     print(num)

# for char in 'hello':
#     if char == 'e':
#         continue
#     else:
#         print(char)


# comma code.

# Input
spam = ['apples', 'bananas', 'tofu', 'cats', 'animas', 'flowers', 'dogs']

# Output
# 'apples, babanas, tofu, and cats'

finalstr = ''

for index in range(len(spam)):  # 0,1,2,3
    if index != len(spam) - 1:  # 3 != 3
        finalstr = finalstr + spam[index] + ', '
    else:
        finalstr = finalstr + ' and ' + spam[index]

print(finalstr)
