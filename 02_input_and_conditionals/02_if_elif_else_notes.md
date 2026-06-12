# Class Notes: If Elif Else

## File

`02_if_elif_else.py`

## What It Is

Conditionals let Python choose what code to run based on whether something is
true or false.

## What It Does

- `if` checks the first condition.
- `elif` checks another condition when the earlier condition is false.
- `else` runs when no earlier condition is true.
- `and` requires all conditions to be true.
- `or` requires at least one condition to be true.

## Why Use It

Most useful programs need decisions. Examples: checking marks, deciding if a
user can get an ID, greeting based on time, or validating a password.

## Example

```python
age = 20
state = 'AP'

if age > 18 and state == 'AP':
    print('Can get ID')
else:
    print('Cannot get ID')
```

## Watch Out For

- Use `==` for comparison, not `=`.
- Indentation is required inside `if`, `elif`, and `else`.
- Put conditions in the correct order.
- `and` is stricter than `or` because every condition must be true.

## Practice

Write a function that receives a temperature and returns `cold`, `warm`, or
`hot`.
