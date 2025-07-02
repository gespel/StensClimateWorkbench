import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
import numpy as np
from math import factorial
import pandas as pd
import crawler


class Plotter:
    def __init__(self, crawler):
        self.crawler = crawler

    def plot_year(self, year, days_window_average=10):
        data = self.crawler.get_historical_temperature(f"{year}-01-01", f"{year}-12-31")
        dates = [i for i in range(0, len(data["hourly"]["time"]))]
        temps = data["hourly"]["temperature_2m"]
        df = pd.DataFrame({"date": dates, "temp": temps})
        df["temp_smooth"] = df["temp"].rolling(window=days_window_average*24, center=True).mean()
        plt.plot(df["date"], df["temp_smooth"], label=year)
        print(f"Plotting done for year {year}")
