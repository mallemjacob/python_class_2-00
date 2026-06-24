import requests

r = requests.get(
    'https://api.github.com/search/repositories?q=language:python+sort:stars')


json_output = r.json()

for i in range(10):
    print(json_output["items"][i]["owner"]["url"])
