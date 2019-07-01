# -*- coding: utf-8 -*-

"""
 ██████╗ ███████╗███╗   ██╗███████╗████████╗██╗ ██████╗     ██████╗██╗████████╗██╗   ██╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝    ██╔════╝██║╚══██╔══╝╚██╗ ██╔╝
██║  ███╗█████╗  ██╔██╗ ██║█████╗     ██║   ██║██║         ██║     ██║   ██║    ╚████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝     ██║   ██║██║         ██║     ██║   ██║     ╚██╔╝
╚██████╔╝███████╗██║ ╚████║███████╗   ██║   ██║╚██████╗    ╚██████╗██║   ██║      ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝     ╚═════╝╚═╝   ╚═╝      ╚═╝

Functions used for evaluation of city populations for algorithm.

By: Andres Rico - aricom@mit.edu
MIT Media Lab - City Science Group
                                                                                      """

import numpy as np
from progressbar import printProgressBar #Import progress bar function.

#Function takes as input a vector with a city design and evaluates ir according to the weoght vector set on objevtive fucntion.
def evaluate(evcity):
    total_evaluation = 0
    wheights = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) #Weights used by function to evaluate. Places more interest in high numbers.
    unique, counts = np.unique(evcity,return_index=False, return_inverse=False, return_counts=True, axis=None)
    dictionary = dict(zip(unique, counts))
    for type in range(1,10):
        #print(dictionary[1])
        if type in evcity:
            total_evaluation = total_evaluation + (dictionary[type] * wheights[type - 1]) #Objective fucntion. This function will change as real city metrics are added to algorithm.
    return total_evaluation

def evaluate_cities(city_to_ev, population ):
    printProgressBar(0, population, prefix = 'Population Evaluation Progress:', suffix = 'Complete', length = 50)
    ev_vector = np.arange(population)
    for pop in range(0, population):
        ev_vector[pop] = evaluate(city_to_ev[pop,:])
        printProgressBar(pop + 1, population, prefix = 'Population Evaluation Progress:', suffix = 'Complete', length = 50)
    return ev_vector
