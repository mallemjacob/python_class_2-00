# Class Notes: Functions Review

## File

`02_functions_review.py`

## What It Is

This lesson reviews functions by showing the same greeting code reused for
different names.

## What It Does

- A function stores reusable code in one place.
- Calling the same function with different arguments changes the output.
- Cleaner code is easier to update.

## Why Use It

If the greeting text needs to change, we only update the function once. Every
function call automatically uses the new behavior.

## Example

```python
def greet(name):
    print('Hi ' + name)

greet('mouse')
greet('cat')
```

## Watch Out For

- Do not copy and paste the same block many times.
- Keep functions small and focused.
- Use parameter names that explain what value is expected.
- Make sure the function is called after it is defined.

## Practice

Create a function named `student_intro(name, course)` that prints three welcome lines for a student.
