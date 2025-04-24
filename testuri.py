# Using requests library
import requests

def generate_completion():
    url = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJkMzllYTA5NC1lM2Y1LTQyZGItYWM1Yi04MzBiNTg1YTAyNjkiLCJwaG9uZSI6Iis5MTk2Njc4MzQ5MzMiLCJpYXQiOjE3NDU0MTAyNzcsImV4cCI6MTc3Njk0NjI3N30.TPPdsSW1VQJkwMXElsgOgZcq0_KvjAatGjN9pmO9t9E"
    }
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Write a poem about artificial intelligence"
            }
        ],
        "model": "gemini-2.0-flash-001",
        "max_tokens": 1000,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    print(data)

generate_completion()