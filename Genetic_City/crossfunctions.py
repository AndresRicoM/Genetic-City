# -*- coding: utf-8 -*-

"""
 ██████╗ ███████╗███╗   ██╗███████╗████████╗██╗ ██████╗     ██████╗██╗████████╗██╗   ██╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝    ██╔════╝██║╚══██╔══╝╚██╗ ██╔╝
██║  ███╗█████╗  ██╔██╗ ██║█████╗     ██║   ██║██║         ██║     ██║   ██║    ╚████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝     ██║   ██║██║         ██║     ██║   ██║     ╚██╔╝
╚██████╔╝███████╗██║ ╚████║███████╗   ██║   ██║╚██████╗    ╚██████╗██║   ██║      ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝     ╚═════╝╚═╝   ╚═╝      ╚═╝

Functions used for crossing individualss in algorithm.

By: Andres Rico - aricom@mit.edu
MIT Media Lab - City Science Group
                                                                                      """
from random import *
from progressbar import printProgressBar #Import progress bar function.
import numpy as np


def cross(parent1, parent2, probability ): #Function takes two parents as inputs and crosses them depending on a certain probability of cross.
    fullarray = np.zeros((2, parent1.shape[0]))
    fullarray[0,:] = parent1
    fullarray[1,:] = parent2

    for inc in range (0, parent1.shape[0]): #Chooses section of individuals to "cut" for cross.
        if random() < probability:
            fullarray[0][inc] = round((parent2[inc]+parent1[inc])/2)
            fullarray[1][inc] = round((parent2[inc]+parent1[inc])/2)

        return fullarray

def cross_individuals(input_city_pop, crossprob, population, citysize): #Complete cross fucntion for an entire population. 
    printProgressBar(0, population, prefix = 'Population Cross Progress:', suffix = 'Complete', length = 50)
    crossed_population = np.zeros((population, citysize*citysize))
    for crosses in range(0,population,2):
        newchildren = cross(input_city_pop[crosses, :], input_city_pop[crosses + 1, :], crossprob)
        crossed_population[crosses,:] = newchildren[0,:]
        crossed_population[crosses + 1,:] = newchildren[1,:]
        printProgressBar(crosses + 2, population, prefix = 'Population Cross Progress:', suffix = 'Complete', length = 50)
    return crossed_population
