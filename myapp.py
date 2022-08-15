import requests

r = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single").json()

print(r["joke"])

