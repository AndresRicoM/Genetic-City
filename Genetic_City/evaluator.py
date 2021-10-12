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

mutation_prob = .9 #Must be between 0 - 1
import numpy as np
from progressbar import printProgressBar #Import progress bar function.

def look_up_table(grid_size):
    source_i_2d=[[i]*grid_size for i in range(grid_size)]
    source_i=[j for sub in source_i_2d for j in sub]
    source_j=list(range(grid_size))*grid_size

    manhattan_distmat=np.array([[np.abs(source_i[ind]-i)+np.abs(source_j[ind]-j) for i in range(grid_size) for j in range(grid_size)] for ind in range(len(source_i))])

    return manhattan_distmat

#Function takes as input a vector with a city design and evaluates it according to the weight vector set on objevtive fucntion.
def evaluate_park(evcity):
    total_evaluation = 0
    wheights = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) #Weights used by function to evaluate. Places more interest in high numbers.
    unique, counts = np.unique(evcity,return_index=False, return_inverse=False, return_counts=True, axis=None)
    dictionary = dict(zip(unique, counts))
    for type in range(1,10):
        #print(dictionary[1])
        if type in evcity:
            total_evaluation = total_evaluation + (dictionary[type] * wheights[type - 1]) #Objective fucntion. This function will change as real city metrics are added to algorithm.
    return total_evaluation #This function should try to give an output of a matrix containing all nines or close to all nines.

def evaluate_balanced(evcity):
    total_evaluation = 0
    wheights = np.array([0, 0, 0, 0, 0, 10, 10, 10, 10]) #Weights used by function to evaluate. Places more interest in high numbers.
    unique, counts = np.unique(evcity,return_index=False, return_inverse=False, return_counts=True, axis=None)
    dictionary = dict(zip(unique, counts))
    for type in range(1,10):
        #print(dictionary[1])
        if type in evcity:
            total_evaluation = total_evaluation + (dictionary[type] * wheights[type - 1]) #Objective fucntion. This function will change as real city metrics are added to algorithm.
    return total_evaluation

def evaluate_simplethree(evcity, look_up):
    unique, counts = np.unique(evcity,return_index=False, return_inverse=False, return_counts=True, axis=None)
    if counts.size < 3:
        evaluation = 0

    else:
        evaluation = 1000 - abs(counts[0]- counts[1]) - abs(counts[0]- counts[2]) - 3*abs(counts[1]- counts[2])


    homes = np.where(evcity == 3)
    offices = np.where(evcity == 1)

    for home in range(int(homes[0].shape[0])):
        for office in range(offices[0].shape[0]):
            evaluation = evaluation - look_up[homes[0][home], offices[0][office]]

    return evaluation


def evaluate_cities(city_to_ev, population, look_up ): #Complete evaluation fucntion for looping through every individual of a population.
    printProgressBar(0, population, prefix = 'Population Evaluation Progress:', suffix = 'Complete', length = 50)
    ev_vector = np.arange(population)
    for pop in range(0, population):
        ev_vector[pop] = evaluate_simplethree(city_to_ev[pop,:], look_up) #Change line to change to desired weight function.
        printProgressBar(pop + 1, population, prefix = 'Population Evaluation Progress:', suffix = 'Complete', length = 50)
    return ev_vector #Returns evaluation vector.
