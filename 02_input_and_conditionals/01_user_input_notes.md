# Class Notes: User Input

## File

`01_user_input.py`

## What It Is

`input()` lets the user type information into the program.

## What It Does

- `input()` always returns a string.
- Use `int()` to convert number text into an integer.
- A function can return an answer instead of printing it directly.
- Conditions can check score ranges.

## Why Use It

User input makes a program interactive. Instead of hardcoding values inside the
file, the program can ask the user for their name, marks, age, or choices.

## Example

```python
marks = int(input('Enter your marks: '))

if marks >= 35:
    print('Pass')
else:
    print('Fail')
```

## Watch Out For

- `input()` gives text, even if the user types a number.
- `int(input())` will crash if the user types letters.
- Add clear prompt messages so users know what to enter.
- Convert input only when you really need a number.

## Practice

Ask the user for their age. Convert it to an integer and print whether they are
older than 18.
