import matplotlib.pyplot as plt
import crawler

class Plotter:
    def __init__(self, crawler):
        self.crawler = crawler

    def plot_year(self, year):
        data = self.crawler.get_historical_temperature(f"{year}-01-01", f"{year}-12-31")
        dates = [i for i in range(0, len(data["hourly"]["time"]))]
        plt.plot(dates, data["hourly"]["temperature_2m"])
        print(f"Plotting done for year {year}")
