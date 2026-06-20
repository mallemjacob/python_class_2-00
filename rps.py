# ROCK PAPER SCISSORS

# r and p -> p
# r and s -> r
# p and r -> p
# p and s -> s
# s and r -> r
# s and p -> s


import random

wins = 0
losses = 0
ties = 0


while True:
    print('ROCK, PAPER, SCISSORS')
    print('SCOREBOARD')
    print("wins: " + str(wins), "losses: " + str(losses), "ties: " + str(ties))
    print('Enter your move: r for rock, p for paper, s for scissors, and q for quit')
    userMove = input()  # r
    if userMove == 'q':
        break
    elif userMove == 'r' or userMove == 'p' or userMove == 's':
        randomNum = random.randint(1, 3)
        if randomNum == 1:
            computerMove = 'r'
        elif randomNum == 2:
            computerMove = 'p'
        elif randomNum == 3:
            computerMove = 's'

        if userMove == 'r' and computerMove == 'p':
            print('ROCK versus PAPER')
            losses = losses + 1
            print('You lost')
        elif userMove == 'r' and computerMove == 's':
            print('ROCK versus SCISSORS')
            wins = wins + 1
            print('You won')
        elif userMove == 'p' and computerMove == 'r':
            print('PAPER versus ROCK')
            wins = wins + 1
            print('You won')
        elif userMove == 'p' and computerMove == 's':
            print('PAPER versus SCISSORS')
            losses = losses + 1
            print('You lost')
        elif userMove == 's' and computerMove == 'r':
            print('SCISSORS versus ROCK')
            losses = losses + 1
            print('You lost')
        elif userMove == 's' and computerMove == 'p':
            print('SCISSORS versus PAPER')
            wins = wins + 1
            print('You won')
        else:
            print(userMove + ' versus ' + computerMove)
            ties = ties + 1
            print("It's a tie")
    else:
        print('Invalid input')
