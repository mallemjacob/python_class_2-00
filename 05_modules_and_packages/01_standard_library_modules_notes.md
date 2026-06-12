# Class Notes: Standard Library Modules

## File

`01_standard_library_modules.py`

## What It Is

A module is a file that contains reusable Python code. The standard library is
the collection of modules that comes with Python.

## What It Does

- `import` brings code from another module into your file.
- `webbrowser` is a built-in Python module.
- Functions can wrap module behavior so code is easier to reuse.
- The `main()` pattern keeps code from running during import.

## Why Use It

Modules save time. Instead of writing everything from scratch, we can use code
Python already provides.

## Example

```python
import webbrowser

webbrowser.open('https://www.python.org')
```

## Watch Out For

- Import the module before using it.
- Some module functions can affect your computer, like opening a browser.
- Put action code inside `main()` when you do not want it to run during import.
- Standard library modules do not need `pip install`.

## Practice

Write a function that receives a search word and opens a Google search URL for
that word.
