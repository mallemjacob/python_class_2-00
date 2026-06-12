# Class Notes: Cat Names List

## File

`03_cat_names_list.py`

## What It Is

This program repeatedly asks the user for names and stores them in a list.

## What It Does

- A `while True` loop can keep asking until the user stops.
- An empty string can be used as a stop signal.
- `in` checks for duplicate names.
- Returning the final list makes the function reusable.

## Why Use It

This pattern is useful whenever we do not know ahead of time how many values the
user wants to enter.

## Example

```python
names = []
name = input('Enter a name: ')

if name not in names:
    names = names + [name]
```

## Watch Out For

- Decide clearly how the user stops the loop.
- Check duplicates before adding a new item.
- Empty strings should not be added as real names.
- For larger programs, `list.append(value)` is more common than
  `list = list + [value]`.

## Practice

Change the program so it stores student names instead of cat names.
