
# -*- coding: utf-8 -*-

"""
 ██████╗ ███████╗███╗   ██╗███████╗████████╗██╗ ██████╗     ██████╗██╗████████╗██╗   ██╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝    ██╔════╝██║╚══██╔══╝╚██╗ ██╔╝
██║  ███╗█████╗  ██╔██╗ ██║█████╗     ██║   ██║██║         ██║     ██║   ██║    ╚████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝     ██║   ██║██║         ██║     ██║   ██║     ╚██╔╝
╚██████╔╝███████╗██║ ╚████║███████╗   ██║   ██║╚██████╗    ╚██████╗██║   ██║      ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝     ╚═════╝╚═╝   ╚═╝      ╚═╝

Genetic algorithm for city design main algorithm code.

By: Andres Rico - aricom@mit.edu Visitng Student MIT Media Lab - City Science Group

Genetic City is a genetic algorithm implementation for aiding in the design of cities. The algorithm creates and evolves a set of possible cities, evaluates their performance and promotes growth of the best evaluated designs.
The algorithm is under development. The basic functions are available for testing but the evaluation function does not yet represent valid city metrics.
Metrics and work is based on concepts and ideas developed by the City Science Group at the MIT Media Lab.
Genetic algorithm for city design main algorithm code.

By: Andres Rico - aricom@mit.edu
MIT Media Lab - City Science Group

"""

import numpy as np                                                              #Matrix and array handling.
import matplotlib.pyplot as plt                                                 #Plotting
from numpy import empty
from citygenerationfunctions import create_cities                               #Functions for creating new city arrays.
from evaluator import evaluate_cities                                           #Functions for evaluation of cities.
from evaluator import evaluate                                                  #Functions for evaluation of cities.
from progressbar import printProgressBar                                        #Helps with progress bar in terminal.
from crossfunctions import cross_individuals                                    #Functions for crossing individuals.
from mutation_functions import mutate_individuals                               #Functions for mutating individuals.
from selectionfunctions import *                                 #Functions for best individual selection.

population_size = 5000 #Needs to be an even number above 4
tournament_individuals = 2 #Needs to be between 2-half of the population.
city_size = 16
mutation_prob = .3 #Must be between 0 - 1
generations = 5000 #Specify number of desired generations
cross_probability = .3 #Uniform crosses

population_matrix = np.arange(city_size * city_size) #Declare different matrix variables for storing populations withing process.
evaluation_vector = np.arange(population_size) #Evaluation vector used for selection.
selected_matrix = np.zeros((population_size, city_size*city_size))
crossed_population_matrix = np.zeros((population_size, city_size*city_size))
mutateded_population_matrix = np.zeros((population_size, city_size*city_size))
best_found_ev = np.zeros(generations) #For Graph
gen = np.arange(generations) + 1
best_found_indiv = np.zeros(city_size * city_size)
best_found_evaluation = 0 #Saves best solution

first_population_flag = True

# Create New Population #################################
population_matrix = create_cities(population_size, city_size)

# Evaluation of First Population ########################
evaluation_vector = evaluate_cities(population_matrix, population_size)

#START OF GENERATON LOOP ################################################################################################################
printProgressBar(0, population_size, prefix = 'Generation Progress:', suffix = 'Complete', length = 50)
for generation in range(0, generations):

    #Selection
    selected_matrix = select_cities_rough(evaluation_vector, population_matrix, population_size, city_size,best_found_indiv,best_found_evaluation)

    #Cross
    crossed_population_matrix = cross_individuals(selected_matrix, cross_probability, population_size, city_size)

    #Mutation
    mutateded_population_matrix = mutate_individuals(crossed_population_matrix, mutation_prob, population_size, city_size)

    # Evaluation of Population
    evaluation_vector = evaluate_cities(mutateded_population_matrix, population_size)


    current_best_individual = mutateded_population_matrix[np.argmax(evaluation_vector),:] #Print best individual from population.
    best_found_ev[generation] = evaluation_vector[np.argmax(evaluation_vector)]
    print('FINISHED GENERATION # ' , generation + 1 , 'OF' , generations) #Counts Generations.
    print('THE HIGHEST EVALUATION OF THIS GENERATION WAS: ' , evaluation_vector[np.argmax(evaluation_vector)])
    print('THIS IS THE BEST CITY DESIGN')
    print(current_best_individual)

    #Save Best Individual if Better than Last
    if evaluation_vector[np.argmax(evaluation_vector)] > best_found_evaluation:
        best_found_evaluation = evaluation_vector[np.argmax(evaluation_vector)]
        print(best_found_evaluation)
        for times in range (0, city_size * city_size):
            best_found_indiv[times] = current_best_individual[times]

print('THE BEST INDIVIDUAL OF ALL WAS:') #Prints and plots final results of algorithm.
print(best_found_indiv)
print('WITH AN EVALUATION OF:')
print(best_found_evaluation)

plt.figure(1)
plt.plot(gen, best_found_ev)
plt.title('Best Found Curve')
plt.ylabel('Evaluation')
plt.xlabel('Generation')
plt.show()
