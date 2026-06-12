import requests
from flask import Flask


app = Flask(__name__)
todo_title = 'No todo loaded yet.'


def get_todo_title(todo_id):
    response = requests.get(
        'https://jsonplaceholder.typicode.com/todos/' + str(todo_id),
        timeout=10,
    )
    response.raise_for_status()

    todo = response.json()
    return todo['title']


@app.route("/")
def hello():
    return todo_title


if __name__ == '__main__':
    user_input = input('Enter a todo number: ')
    todo_title = get_todo_title(user_input)
    app.run(debug=True)
