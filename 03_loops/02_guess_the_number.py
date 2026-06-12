"""Lesson 6: a guess-the-number game with loops."""

import random


def play_game():
    random_number = random.randint(1, 20)

    print('I am thinking of a number between 1 and 20.')

    for attempt in range(1, 6):
        user_guess = int(input('Guess the number: '))

        if random_number > user_guess:
            print('Your guess is too low.')
        elif random_number < user_guess:
            print('Your guess is too high.')
        else:
            print('You guessed it in ' + str(attempt) + ' tries.')
            return

    print('Game over. The number was ' + str(random_number) + '.')


if __name__ == '__main__':
    play_game()
