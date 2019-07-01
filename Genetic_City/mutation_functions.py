import numpy as np
from random import *
from random import random
from random import randint

def mutation(input_city, mut_prob):
    for genes in range(0, input_city.shape[0]):
        if random() < mut_prob :
            #place_variable = randint(1,9)
            input_city[genes] = randint(1,9)
            #print('Mutated Gene!')
    return input_city
