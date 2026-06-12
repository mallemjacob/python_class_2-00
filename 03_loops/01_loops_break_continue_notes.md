# Class Notes: Loops Break Continue

## File

`01_loops_break_continue.py`

## What It Is

Loops repeat code. Python has `while` loops and `for` loops.

## What It Does

- A `while` loop runs while a condition is true.
- A `for` loop is useful when you know how many times to repeat.
- `break` exits a loop early.
- `continue` skips the rest of the current loop step.
- `range()` creates a sequence of numbers.

## Why Use It

Loops help us avoid duplicate code. They are useful for counting, retrying,
reading lists, building games, and repeating actions until a condition changes.

## Example

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

## Watch Out For

- A `while` loop can run forever if the condition never becomes false.
- Update counter variables inside `while` loops.
- `break` stops the loop completely.
- `continue` skips only the current loop step.
- `range(1, 6)` gives `1, 2, 3, 4, 5`, not `6`.

## Practice

Print numbers from 1 to 20, but skip numbers from 8 to 12.
