
import requests
class Giphy:
    def get_url(self, search_word):
        api = "api_key"
        gif = requests.get(url="https://api.giphy.com/v1/gifs/translate", params={"api_key": api, "s":search_word})
        gif_url = gif.json()["data"]["images"]["original"]["mp4"]
        return gif_url

    def get_joke(self):
        joke = requests.get(url="end_point",
                            headers={"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com",
                                     "X-RapidAPI-Key": "api_key"})
        setup = joke.json()["body"][0]["setup"]
        punchline = joke.json()["body"][0]["punchline"]
        return (setup, punchline)


    def location(self):
        iss = requests.get(url="http://api.open-notify.org/iss-now.json").json()
        long = iss["iss_position"]["longitude"]
        lat = iss["iss_position"]["latitude"]
        return (lat, long)



