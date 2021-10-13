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


def city_plot(input_city, block_size, grid_size ):
    size = block_size * grid_size
    plt.style.use('dark_background')
    print(input_city.shape)
    Z = input_city.reshape((size, size))
    x = np.arange(0, size+1, 1)  # len = 11
    y = np.arange(0, size+1, 1)  # len = 7
    X, Y = np.meshgrid(x, y)
    X = X + 0.2 * Y  # tilt the coordinates.
    Y = Y + 0.3 * X
    fig, ax = plt.subplots()
    for i in range(grid_size+1):
        ax.plot(np.arange(size+1), np.repeat(i*block_size,size+1), linewidth = '5', color = 'gray')
        ax.plot(np.repeat(i*block_size,size+1), np.arange(size+1),  linewidth = '5', color = 'gray')
    ax.pcolormesh(x, y, Z, cmap='rainbow',edgecolors='k', linewidths=2)
    plt.axis('off')

    plt.show()

    return
