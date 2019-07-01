import numpy as np
from random import *

def cross(parent1, parent2, probability ):
    fullarray = np.zeros((2, parent1.shape[0]))
    fullarray[0,:] = parent1
    fullarray[1,:] = parent2

    for inc in range (0, parent1.shape[0]):
        if random() < probability:
            fullarray[0][inc] = round((parent2[inc]+parent1[inc])/2)
            fullarray[1][inc] = round((parent2[inc]+parent1[inc])/2)

        return fullarray
