import time
from multiprocessing.spawn import freeze_support
from os import path
import os
from flask import Flask, render_template, request, jsonify, app
import matplotlib.pyplot as plt
import multiprocessing
from plotter import Plotter
from crawler import Crawler

app = Flask(__name__)

def plot_years(filename, start, end):
    c = Crawler()
    p = Plotter(c)
    plt.figure(figsize=(18, 8))
    for y in range(start, end):
        p.plot_year(y, days_window_average=20)
    plt.legend()
    plt.savefig(f"{filename}.svg")
    plt.close()

def time_plot_loop(filename, start, stop, wait):
    while True:
        plot_years(filename, start, stop)
        print("Plotted a new graph.")
        time.sleep(wait)

def start_plotting_process(start, end):
    if not path.exists(f"static"):
        os.mkdir("static")

    p = multiprocessing.Process(target=time_plot_loop, args=("static/plot", start, end, 7200))
    p.start()

@app.route('/')
def index():
    return "<center><img src='static/plot.svg'></center>"


if __name__ == "__main__":
    freeze_support()
    start_plotting_process(2020, 2025)
    app.run("0.0.0.0", 80)