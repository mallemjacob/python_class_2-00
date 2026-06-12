import requests

result = requests.get('https://jsonplaceholder.typicode.com/todos/1')

jsonResult = result.json()

print(jsonResult)
