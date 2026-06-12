# Class Notes: Nested Loops

## File

`03_nested_loops.py`

## What It Is

A nested loop is a loop inside another loop.

## What It Does

- The inner loop runs completely for each step of the outer loop.
- A flag variable can remember that a target was found.
- `break` exits only the current loop, so the outer loop needs its own check.

## Why Use It

Nested loops are useful when working with rows and columns, tables, grids,
patterns, coordinates, and combinations.

## Example

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row, column)
```

## Watch Out For

- The inner loop repeats many times, so output can grow quickly.
- `break` only exits the loop it is directly inside.
- Use clear variable names like `row` and `column`.
- A flag variable can help stop both loops when needed.

## Practice

Print all row and column pairs from 1 to 5. Stop when row is 3 and column is 4.
