import requests

url = 'http://localhost:9697/predict'

data = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=data)
predictions = response.json()

print(predictions)
