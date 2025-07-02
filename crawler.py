import requests
import matplotlib.pyplot as plt

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

    def get_historical_temperature(self, start, end):
        response = requests.get(
            f"https://archive-api.open-meteo.com/v1/era5?latitude=52.52&longitude=13.41&start_date={start}&end_date={end}&hourly=temperature_2m")
        if response.status_code == 200:
            return response.json()
        return None

if __name__ == "__main__":
    c = Crawler()
    data = c.get_historical_temperature("2021-01-01", "2021-01-31")
    plt.plot(data["hourly"]["time"], data["hourly"]["temperature_2m"])
    plt.show()