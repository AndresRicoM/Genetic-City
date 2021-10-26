import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np
import os

rows=12
cols=12

class Grid:
    def __init__(self, rows, cols, grid_types):
        self.rows=rows
        self.cols=cols
        self.grid_types=grid_types

    def generate_dist_mat(self):
        source_i_2d=[[i]*self.cols for i in range(self.rows)]
        source_i=[j for sub in source_i_2d for j in sub]
        source_j=list(range(self.cols))*self.rows

        manhattan_distmat=np.array([[np.abs(source_i[ind]-i)+np.abs(source_j[ind]-j) for i in range(rows) for j in range(cols)
                           ] for ind in range(len(source_i))])
        return manhattan_distmat


    def generate_od(self, source_id, dest_id, power=1):
        origin_mask=(np.array(self.grid_types)==source_id).astype(int)
        destination_mask=(np.array(self.grid_types)==dest_id).astype(int)
        manhattan_distmat=self.generate_dist_mat()

        od=1/np.power(manhattan_distmat, power) # initialise OD as inverse of friction function
        od=np.multiply(od, destination_mask) # non-dest cols to zero
        od=np.multiply(od.T, origin_mask).T # non-source rows to zero

        od=np.nan_to_num(od, nan=0, posinf=0) # Convert inf (trips with zero friction. i.e. to and from same cell) to zero

        # Furness method
        for i in range(10):
            sum_each_col=od.sum(axis=0)
            sum_each_col[sum_each_col==0]=1 # to avoid division by zero error- multiplying zero by 1 wont make a difference anyway
            od=np.multiply(od, 1/sum_each_col)

            sum_each_row=od.sum(axis=1)
            sum_each_row[sum_each_row==0]=1
            od=np.multiply(od.T, 1/sum_each_row).T
        return od

    def plot_grid(self, colors):
        plt.figure(figsize=(12,12))
        cell_cols=[colors[c] for c in self.grid_types]
        X=[ind%cols for ind in range(len(self.grid_types))]
        Y=[int(ind/cols)for ind in range(len(self.grid_types))]
        plt.scatter(X, Y, color=cell_cols, marker='s', s=1300)


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

def load_grid_data(file_loc):
    with open(file_loc) as f:
        lines = f.readlines()
        grid_list=[]
    for line in lines:
        grid_list.extend([int(n.split('.')[0]) for n in line.split(',')])
    return grid_list

def grid_plot():
    #plt.style.use('dark_background')

    colors=['white', 'purple', 'green', 'red']
    city_n=1
    directory = '/Users/AndresRico/Desktop/working/Genetic-City/Genetic_City/plotting'

    for files in os.listdir(directory):
        f = os.path.join(directory, files)
        print(f)
        print(files)
        if os.path.isfile(f) and files != '.DS_Store':

            grid_list=load_grid_data(f.format(city_n))

            grid=Grid(12, 12, grid_list)
            grid.plot_grid(colors)
            plt.savefig('/Users/AndresRico/Desktop/working/Genetic-City/Genetic_City/images/'+str(files)+'.png')

grid_plot()
