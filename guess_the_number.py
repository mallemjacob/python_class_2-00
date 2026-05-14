import random
secretNumber = random.randint(1, 20)  # 15


for i in range(1, 11):  # 1,2,3
    print('I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    user_input = int(input())  # 7

    if user_input > secretNumber:  # 17 > 15
        print('Your guess is too high.')
    elif user_input < secretNumber:  # 7 < 15
        print('Your guess is too low.')
    else:
        print('Your guess is correct')
        break

print('You guessed the number in ' + str(i) + ' guesses')
# to move all lines to the right side
# press shift and select all the lines you want to move.
# then press Tab key


# for i in range(1, 6):  # 1,2,3,4,5
#     print(i)
