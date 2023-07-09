import requests
import json


response = requests.get('https://jsonplaceholder.typicode.com/todos/')


print(response.status_code)


response = json.loads(response.text)

for data in response:
    print(data)
