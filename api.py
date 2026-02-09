import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

"""print(response.status_code)
print(response.text[:200])"""
data = response.json()

print("setup: ", data["setup"])
print("punchline: ", data["punchline"])