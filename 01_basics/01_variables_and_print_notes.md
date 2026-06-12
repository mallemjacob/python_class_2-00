# Class Notes: Variables And Print

## File

`01_variables_and_print.py`

## What It Is

Variables are names that store values. `print()` is a built-in function that
shows output on the screen.

```python
name = 'mouse'
age = 25
print(name)
```

## What It Does

- Stores information so we can reuse it later.
- Gives values meaningful names.
- Sends output to the terminal using `print()`.
- Combines text values using string concatenation.

## Why Use It

Without variables, we would have to type the same values again and again.
Variables make programs easier to read, update, and understand.

## Example

```python
first_name = 'valkyrie'
last_name = 'loki'
age = 30

full_name = first_name + ' ' + last_name
print('I am ' + full_name)
print('I am ' + str(age) + ' years old')
```

## Watch Out For

- Text must be inside quotes.
- Variable names cannot contain spaces.
- Python is case-sensitive: `name` and `Name` are different.
- You cannot directly join a string and an integer. Use `str(age)`.

## Practice

Create variables for your first name, last name, and age. Print one sentence
that says your full name and another sentence that says your age next year.
