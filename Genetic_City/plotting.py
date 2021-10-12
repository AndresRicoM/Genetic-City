import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np


def plot_best_found_curve(generations, best_found):

    plt.style.use('dark_background')
    plt.figure(1)
    plt.plot(generations, best_found)
    plt.title('Best Found Curve')
    plt.ylabel('Evaluation')
    plt.xlabel('Generation')
    plt.show()

    return


def city_plot(input_city, size):
    plt.style.use('dark_background')
    print(input_city.shape)
    Z = input_city.reshape((size, size))
    x = np.arange(0, size+1, 1)  # len = 11
    y = np.arange(0, size+1, 1)  # len = 7
    fig, ax = plt.subplots()
    ax.pcolormesh(x, y, Z, cmap='rainbow')
    plt.show()

    return
