# Generate a random number. 1,20 -> 10
# Store it in a variable.

# Ask user to guess the number 15
# usernumber
# if randomnumber is equal to usernumber
# if randomnumber is greater than usernumber, your guess too low.
# if randomnumber is less than usernumber, your guess too high.


import random
random_number = random.randint(1, 20)


print('I am thinking of a number between 1 and 20.')

# while True:
for i in range(1, 6):  # 1,2,3,4,5
    print('Guess the number')
    user_guess = int(input())  # 13

    if random_number > user_guess:
        print('Your guess is too low.')
    elif random_number < user_guess:
        print('Your guess is too high.')
    elif random_number == user_guess:
        print('You have guessed in ' + str(i) + ' tries.')
        break

if i < 5:
    print('Your guess is correct')
else:
    print('You havent guessed. The game is over.')

print('The end')
