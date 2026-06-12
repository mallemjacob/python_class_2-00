# Class Notes: Try Except

## File

`01_try_except.py`

## What It Is

Error handling lets a program respond to problems instead of crashing.

## What It Does

- `try` contains code that might fail.
- `except` handles a specific error.
- `ZeroDivisionError` happens when dividing by zero.
- `TypeError` happens when a value is the wrong type for an operation.
- `continue` can skip part of a loop.

## Why Use It

Users can enter unexpected values, files can be missing, internet requests can
fail, and math can be invalid. Error handling keeps the program controlled and
gives useful messages.

## Example

```python
try:
    answer = 10 / number
except ZeroDivisionError:
    answer = 'Cannot divide by zero'
```

## Watch Out For

- Catch specific errors when possible.
- Avoid using a bare `except:` because it can hide real bugs.
- `try` should contain only the risky code, not the whole program.
- Error messages should help the user understand what went wrong.
- Some errors, like syntax errors, should be fixed in code instead of handled
  with `except`.

## Practice

Ask the user for two numbers and divide them. Handle division by zero and text
input safely.
