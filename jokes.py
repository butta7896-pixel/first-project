import requests

def tatti():
    url = "https://official-joke-api.appspot.com/random_joke"

    joke = requests.get(url)

    if joke.status_code == 200:
        json = joke.json()
        jokeQuestion = json["setup"]
        jokeAnswer = json["punchline"]

        print("\nJughat:")
        print(jokeQuestion)
        input("\n(press Enter for the punchline...)")
        print(jokeAnswer)
    else:
        print("Couldn't fetch a joke right now. Try again!")

tatti()
