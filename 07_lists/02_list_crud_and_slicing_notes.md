# Class Notes: List CRUD And Slicing

## File

`02_list_crud_and_slicing.py`

## What It Is

CRUD means Create, Read, Update, and Delete. These are the common actions we do
with list data.

## What It Does

- Create: make a list or add an item.
- Read: access an item by index.
- Update: assign a new value to an index.
- Delete: use `del`.
- Slicing returns part of a list.
- `in` checks whether an item exists in a list.

## Why Use It

Most programs need to manage collections of data. Lists let us add, change,
remove, search, and loop through those values.

## Example

```python
fruits = ['apples', 'bananas', 'grapes']
fruits = fruits + ['oranges']
fruits[1] = 'kiwi'
del fruits[0]
print(fruits[0:2])
```

## Watch Out For

- Updating or deleting needs a valid index.
- Slicing does not include the ending index.
- `fruits[0:3]` returns indexes `0`, `1`, and `2`.
- `in` checks exact values, so spelling matters.
- Be careful when changing a list while looping over it.

## Practice

Create a list of six cities. Replace one city, delete one city, print a slice,
and check whether a city exists in the list.
