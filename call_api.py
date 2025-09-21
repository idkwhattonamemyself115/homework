import requests
url = "http://127.0.0.1:5000/api/joke"
response = requests.get(url)
data = response.json()
print(data)
# Use requests package to call your api address http://127.0.0.1:5000/api/joke to display a funny joke

