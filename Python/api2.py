import requests
try:

    response = requests.get("https://official-joke-api.appspot.com/random_joke")

    if response.status_code == 200:
        data = response.json()
        print( data["setup"])
        print( data["punchline"])
    else:
        print("API failed with code: ", response.status_code)
    
except requests.exceptions.RequestException:
    print("Network error!")
