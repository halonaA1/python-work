import sys
import matplotlib.pyplot as plot
import random
import string
import numpy as np

def plot_lines():
    x = np.linspace(0, 2 *np.pi, 200)
    print(f"{x = }")
    y = np.sin(x)
    fig, ax = plot.subplots()
    print(f"{type(fig) = }; {type(ax) = }")
    ax.plot(x, y)
    plot.show()

def plot_scutter():
    x = [random.random() for _ in range(30)]
    y = [random.random() for _ in range(30)]
    fig, ax = plot.subplots()
    ax.scatter(x, y)
    plot.show()

def plot_barchart():
    x = [random.randint(10, 100) for _ in range(10)]
    y = list(string.ascii_uppercase[:10])
    fig, ax = plot.subplots()
    ax.bar(y, x)
    plot.show()

def plot_histogram():
    data = [random.gauss(0, 1) for _ in range(1000)]
    fig, ax = plot.subplots()
    n, bins, patches = ax.hist(data, 20, density=True)
    plot.show()

def plot_boxplot():
    data = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25),  (100, 3))
    fig, ax = plot.subplots()
    bplot = ax.boxplot(data)
    plot.show()

def plot_multiplot_and_export():
    fig, axs = plot.subplots(1,2)
    x1 = [3, 5]
    y1 = [5, 2]
    x2 = [3, 5]
    y2 = [8, 2]
    axs[0].plot(x1, y1)
    axs[1].scatter(x2, y2)
    plot.show()
    fig.savefig('plot_multiplot_and_export.png')
    plot.close(fig)

def plot_legend():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    z = np.cos(x)
    fig, ax = plot.subplots()
    ax.plot(x, y, label="sin(x)")
    ax.plot(x, z,label="cos(x)")
    ax.legend()
    plot.show()

def plot_title_and_text():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    z = np.cos(x)
    fig, ax = plot.subplots()
    ax.plot(x, y, label="sin(x)")
    ax.plot(x, z, label="cos(x)")
    ax.legend()
    ax.set_title("plot Title")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plot.show()

def plot_axes():
    fig, ax = plot.subplots()
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    z = np.cos(x)
    ax.plot(x, y, label="sin(x)")
    ax.plot(x, z, label="cos(x)")
    ax.legend()
    ax.set_title("plot title")
    #fig.subtitle("Useful for multiple plots")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, linestyle="-.")
    ax.tick_params(axis ="y", labelcolor="r", labelsize="medium", width=3)
    ax.set_xlim(6,0)
    ax.axhline(0, color="black", linewidth=2)
    plot.show()

def main():
    plot_lines()
    plot_scutter()
    plot_barchart()
    plot_histogram()
    plot_boxplot()
    plot_multiplot_and_export()
    plot_legend()
    plot_title_and_text()
    plot_axes()
    return 0

if __name__ == "__main__":
    sys.exit(main())
