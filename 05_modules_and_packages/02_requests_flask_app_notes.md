# Class Notes: Requests And Flask App

## File

`02_requests_flask_app.py`

## What It Is

Third-party packages are extra tools installed from outside Python's standard
library. `requests` helps call websites/APIs. `Flask` helps create a small web
app.

## What It Does

- `requests.get()` calls an API.
- `.json()` converts a JSON response into Python data.
- `Flask(__name__)` creates a small web app.
- `@app.route("/")` defines what the homepage returns.
- Third-party packages should be installed inside a virtual environment.

## Why Use It

Real programs often need to get data from the internet and show it in a web
page. This lesson connects API data to a simple Flask website.

## Example

```python
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
todo = response.json()
print(todo['title'])
```

## Watch Out For

- Install packages before importing them: `pip install requests flask`.
- Internet requests can fail, so real apps should handle errors.
- Use `timeout` so a request does not wait forever.
- Use `response.raise_for_status()` to catch bad HTTP responses.
- Do not put secret API keys directly in class files.

## Practice

Change the Flask route to show both the todo title and whether it is completed.
