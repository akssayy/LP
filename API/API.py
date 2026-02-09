import requests

try:
    num = int(input("How many jokes joke: "))

    if num <= 0:
        print("Number must be positive !")
        exit()

except ValueError:
    print("Invalid Choice, Enter a number")
    num = 0

for i in range(num):
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke",
        timeout = 5)

        if response.status_code == 200:
            data = response.json()
            print("\nsetup:", data["setup"])
            print("punchline:", data["punchline"])

        else:
            print("API error:", response.status_code)

    except requests.exceptions.RequestException:
        print("Network error!")