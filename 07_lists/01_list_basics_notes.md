# Class Notes: List Basics

## File

`01_list_basics.py`

## What It Is

A list stores multiple values in one variable.

## What It Does

- A list stores many related values.
- List indexes start at `0`.
- `len(list_name)` returns the number of items.
- `list_name[-1]` gets the last item.

## Why Use It

Lists are useful when one variable needs to hold many related values, like
student names, marks, shopping items, or languages.

## Example

```python
animals = ['cat', 'rat', 'bat']
print(animals[0])
print(animals[-1])
```

## Watch Out For

- The first item is index `0`, not index `1`.
- Accessing an index that does not exist causes an error.
- `len(animals)` gives the count, but the last index is `len(animals) - 1`.
- Negative indexes count from the end of the list.

## Practice

Create a list of five favorite foods. Print the first item, last item, and list
length.
