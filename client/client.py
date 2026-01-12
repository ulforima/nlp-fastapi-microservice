import requests

URL = "http://127.0.0.1:8000/corpus"

corpus = [
    "Natural language processing is fun",
    "FastAPI is a modern web framework",
    "NLP uses statistics and machine learning"
]

response = requests.post(URL, json={"texts": corpus})

print("Status code:", response.status_code)
print("Response:", response.json())
