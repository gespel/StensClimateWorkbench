import requests

class Crawler:
    def __init__(self):
        self.latitude = 51.1657
        self.longitude = 10.4515
        self.url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={self.latitude}&longitude={self.longitude}"
            f"&current=temperature_2m"
        )

    def get_temperature_germany(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception(f"API-Anfrage fehlgeschlagen mit Statuscode {response.status_code}")

        data = response.json()

        try:
            temperature = data["current"]["temperature_2m"]
            time = data["current"]["time"]
            print(f"Aktuelle Temperatur in Deutschland (Zentrum) um {time}: {temperature}°C")
        except KeyError:
            print("Fehler beim Auslesen der Temperaturdaten.")
            print(data)