# Set

an unordered collection of unique items.
fast for checking if an item exists.
removing duplicates.

## Creating a set

my_numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}

### empty set

empty_set = set()

## convert list with duplicates to set

my_list = [1, 2, 2, 3, 3, 3, 4]
my_set = set(my_list)

## Modifying a Set

### Add a single item

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

### remove a single item

fruits.remove("orange")
fruits.discard("orange")

## Set Operations

math_students = {"Alice", "Bob", "Charlie"}
science_students = {"Bob", "Charlie", "David"}

### Union (|): Combines everything from both sets (no duplicates).

`math_students | science_students`
`{'Alice', 'Bob', 'Charlie', 'David'}`

### Intersection (&): Only items that exist in both sets.

`math_students & science_students`
`{'Bob', 'Charlie'}`

### Difference (-): Items in the first set, but NOT in the second set.

`math_students - science_students`
`{'Alice'}`

### Symmetric Difference (^): Items in either set, but NOT in both (the exact opposite of intersection).

`math_students ^ science_students`
`{'Alice', 'David'}`

## Frozensets

Normal sets are mutable
You cannot change it.

```python
vowels = frozenset(["a", "e", "i", "o", "u"])
print(vowels)

my_dictionary = {
    vowels: "These are the English vowels"
}
print(my_dictionary[vowels])
```

```python
flight_distances = {
    frozenset({"New York", "London"}): 3459,  # Miles
    frozenset({"Tokyo", "San Francisco"}): 5118
}


# New York to London
search_1 = frozenset({"New York", "London"})
print(flight_distances[search_1])
# Output: 3459

# London to New York
search_2 = frozenset({"London", "New York"})
print(flight_distances[search_2])
# Output: 3459
```

---

# Comprehensions

Python's built-in shortcut for making a new list (or set) out of an old one.

```python
numbers = [1, 2, 3, 4]
doubled_numbers = []

for x in numbers:
    if x % 2 == 0:
        doubled_numbers.append(x * 2)

print(doubled_numbers)
# Output: [2, 4, 6, 8]

```

## List Comprehension

```python
numbers = [1, 2, 3, 4]
doubled_numbers = [x * 2 for x in numbers]

print(doubled_numbers)
# Output: [2, 4, 6, 8]
```

### Adding a Condition

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {x**2 for x in numbers if x % 2 == 0}
```

## Set Comprehension

```python
my_set = {x for x in [1, 1, 2, 2, 3]}
```

---
