# for loops


# while condition:
#     code block

# i = 0
# while i < 10:
#     print('hi')
#     i = i + 1


# for count in range(10):  # 0..9
#     print('hi')

# for count in range(5, 10):
#     print(count)


# break = exit out of loop
# continue = skip a step in a loop

# for count in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     if count == 5:
#         break
#     else:
#         print(count)

# for count in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     if count == 5:
#         continue
#     else:
#         print(count)


# Homework
# Add for loop for username input for the program below.


# while True:
#     print('Enter your age: ')
#     age = int(input())
#     if age > 18:
#         print('enter you username')
#         username = input()
#         if username == 'peppy':
#             for i in range(1, 4):  # 1,2,3
#                 print('Enter you password')
#                 password = input()
#                 if password == 'killer':
#                     print('welcome')
#                     break
#                 else:
#                     print('wrong password')
#                     print('You only have ' + str(3 - i) + ' attempt left')
#             break
#         else:
#             print('Wrong username')
#     else:
#         print('you have to be above 18 years old.')
