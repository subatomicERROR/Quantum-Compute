import requests

url = "http://localhost:8000/quantum-compute/"
data = {"data": "quantum data example"}

response = requests.post(url, json=data)
print(response.json())
