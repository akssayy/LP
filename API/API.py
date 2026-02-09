import requests

input("press enter for a joke")

try:
    response = requests.get("https://official-joke-api.appspot.com/random_joke")

    if response.status_code == 200:
        data = response.json()
        print("setup:", data["setup"])
        print("punchline:", data["punchline"])

    else:
        print("API error:", response.status_code)

except requests.exceptions.RequestException:
    print("Network error!")