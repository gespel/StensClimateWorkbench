import matplotlib.pyplot as plt

from plotter import Plotter
from crawler import Crawler

def plot_years(filename, start, end):
    c = Crawler()
    p = Plotter(c)

    for y in range(start, end):
        p.plot_year(y, days_window_average=20)
    plt.legend()
    plt.savefig(f"{filename}.svg")

plot_years("test", 2020, 2024)