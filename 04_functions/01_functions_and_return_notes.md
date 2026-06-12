# Class Notes: Functions And Return

## File

`01_functions_and_return.py`

## What It Is

A function is a named block of reusable code.

## What It Does

- `def` creates a function.
- Parameters receive values.
- Arguments are values passed during a function call.
- Default values are used when no argument is provided.
- `return` sends a value back to the caller.
- `*numbers` accepts many arguments.

## Why Use It

Functions help avoid repeated code. They make programs easier to read, test,
reuse, and fix.

## Example

```python
def add_numbers(a, b):
    return a + b

answer = add_numbers(10, 20)
print(answer)
```

## Watch Out For

- Defining a function does not run it. You must call it.
- `return` gives a value back; `print()` only displays a value.
- Code after `return` inside the same function will not run.
- Default arguments should come after required arguments.
- Function names should clearly describe what the function does.

## Practice

Write a function called `multiply_many()` that accepts any amount of numbers and returns their product.
