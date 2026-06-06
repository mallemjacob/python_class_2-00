import requests
from flask import Flask


print('Enter a number: ')
user_input = input()  # '4;
response = requests.get(
    'https://jsonplaceholder.typicode.com/todos/' + user_input)

# convert the return response in a readble format
converted_response = response.json()

app = Flask(__name__)


@app.route("/")
def hello():
    return converted_response['title']
