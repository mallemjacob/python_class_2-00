# Class Notes: Guess The Number

## File

`02_guess_the_number.py`

## What It Is

This is a small game where the computer chooses a random number and the user
tries to guess it.

## What It Does

- `random.randint(1, 20)` gives a random number between 1 and 20.
- A `for` loop limits the player to five guesses.
- `int(input())` converts the user's guess into a number.
- `return` can leave a function early when the game is won.

## Why Use It

This lesson combines several important skills in one useful program: importing
a module, asking for input, comparing numbers, using loops, and stopping early.

## Example

```python
secret_number = random.randint(1, 20)
guess = int(input('Guess the number: '))

if guess < secret_number:
    print('Too low')
```

## Watch Out For

- Import `random` before using it.
- Convert the guess with `int()` before comparing it to a number.
- The game should stop when the user guesses correctly.
- The game should also stop after the allowed number of attempts.
- Text input will cause an error unless you add error handling.

## Practice

Change the game to use numbers from 1 to 50 and allow seven guesses.
