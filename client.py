import requests

response = requests.post('http://127.0.0.1:5000/authorize', json={
    "card": "4111111111111111",
    "amount": 100.50
})

print(response.json())