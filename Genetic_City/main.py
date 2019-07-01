
# -*- coding: utf-8 -*-

"""
 ██████╗ ███████╗███╗   ██╗███████╗████████╗██╗ ██████╗     ██████╗██╗████████╗██╗   ██╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝    ██╔════╝██║╚══██╔══╝╚██╗ ██╔╝
██║  ███╗█████╗  ██╔██╗ ██║█████╗     ██║   ██║██║         ██║     ██║   ██║    ╚████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝     ██║   ██║██║         ██║     ██║   ██║     ╚██╔╝
╚██████╔╝███████╗██║ ╚████║███████╗   ██║   ██║╚██████╗    ╚██████╗██║   ██║      ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝     ╚═════╝╚═╝   ╚═╝      ╚═╝

Genetic algorithm for city design main algorithm code.

By: Andres Rico - aricom@mit.edu
MIT Media Lab - City Science Group
                                                                                      """

import numpy as np
import matplotlib.pyplot as plt
from numpy import empty
from citygenerationfunctions import create_cities
from evaluator import evaluate_cities
from evaluator import evaluate
from progressbar import printProgressBar
from selectionfunctions import match
from crossfunctions import cross
from mutation_functions import mutation

population_size = 100 #Needs to be an even number above 4
city_size = 100
mutation_prob = .9 #Must be between 0 - 1
generations = 1000 #Specify number of desired generations
cross_probability = .2 #Uniform crosses

population_matrix = np.arange(city_size * city_size)
evaluation_vector = np.arange(population_size)
selected_population_matrix = np.zeros((population_size, city_size*city_size))
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

#START OF GENRATON LOOP ################################################################################################################
printProgressBar(0, population_size, prefix = 'Generation Progress:', suffix = 'Complete', length = 50)
for generation in range(0, generations):

    #Selection
    #selected_population_matrix = np.zeros((population_size, city_size*city_size))
    printProgressBar(0, population_size, prefix = 'Population Evaluation Progress:', suffix = 'Complete', length = 50)
    for tournaments in range(0, population_size):
        if tournaments >= (population_size - 3):
            if tournaments == population_size - 3:
                winner = match(evaluation_vector[0], evaluation_vector[tournaments], evaluation_vector[tournaments + 1], evaluation_vector[tournaments + 2] )
            if tournaments == population_size - 2:
                winner = match(evaluation_vector[0], evaluation_vector[1], evaluation_vector[tournaments], evaluation_vector[tournaments + 1] )
            if tournaments == population_size - 1:
                winner = match(evaluation_vector[0], evaluation_vector[1], evaluation_vector[2], evaluation_vector[tournaments] )

            if winner == 0:
                selected_population_matrix[tournaments,:] = population_matrix[0]
            if winner == 1:
                selected_population_matrix[tournaments,:] = population_matrix[tournaments]
            if winner == 2:
                selected_population_matrix[tournaments,:] = population_matrix[0]
            if winner == 3:
                selected_population_matrix[tournaments,:] = population_matrix[tournaments]

        else:
            winner = match(evaluation_vector[tournaments], evaluation_vector[tournaments + 1], evaluation_vector[tournaments + 2], evaluation_vector[tournaments + 3])
            if winner == 0:
                selected_population_matrix[tournaments,:] = population_matrix[tournaments]
            if winner == 1:
                selected_population_matrix[tournaments,:] = population_matrix[tournaments + 1]
            if winner == 2:
                selected_population_matrix[tournaments,:] = population_matrix[tournaments + 2]
            if winner == 3:
                selected_population_matrix[tournaments,:] = population_matrix[tournaments + 3]

        printProgressBar(tournaments + 1, population_size, prefix = 'Population Selection Progress:', suffix = 'Complete', length = 50)

    #print(selected_population_matrix)

    #Cross
    printProgressBar(0, population_size, prefix = 'Population Cross Progress:', suffix = 'Complete', length = 50)
    for crosses in range(0,population_size,2):
        newchildren = cross(selected_population_matrix[crosses, :], selected_population_matrix[crosses + 1, :], cross_probability)
        crossed_population_matrix[crosses,:] = newchildren[0,:]
        crossed_population_matrix[crosses + 1,:] = newchildren[1,:]
        printProgressBar(crosses + 2, population_size, prefix = 'Population Cross Progress:', suffix = 'Complete', length = 50)

    #Mutation
    printProgressBar(0, population_size, prefix = 'Population Mutation Progress:', suffix = 'Complete', length = 50)
    for indiv in range (0, population_size):
        #print(crossed_population_matrix[indiv, :])
        mutated_individual = mutation(crossed_population_matrix[indiv, :], mutation_prob)
        mutateded_population_matrix[indiv, :] = mutated_individual
        #print(mutateded_population_matrix[indiv, :])
        printProgressBar(indiv + 1, population_size, prefix = 'Population Mutation Progress:', suffix = 'Complete', length = 50)


    # Evaluation of Population
    evaluation_vector = evaluate_cities(mutateded_population_matrix, population_size)


    current_best_individual = mutateded_population_matrix[np.argmax(evaluation_vector),:]
    best_found_ev[generation] = evaluation_vector[np.argmax(evaluation_vector)]
    print('FINISHED GENERATION # ' , generation + 1 , 'OF' , generations)
    print('THE HIGHEST EVALUATION OF THIS GENERATION WAS: ' , evaluation_vector[np.argmax(evaluation_vector)])
    print('THIS IS THE BEST CITY DESIGN')
    print(current_best_individual)

    #Save Best Individual if Better than Last
    if evaluation_vector[np.argmax(evaluation_vector)] > best_found_evaluation:
        best_found_evaluation = evaluation_vector[np.argmax(evaluation_vector)]
        print(best_found_evaluation)
        for times in range (0, city_size * city_size):
            best_found_indiv[times] = current_best_individual[times]

print('THE BEST INDIVIDUAL OF ALL WAS:')
print(best_found_indiv)
print('WITH AN EVALUATION OF:')
print(best_found_evaluation)


plt.figure(1)
plt.plot(gen, best_found_ev)
plt.title('Best Found Curve')
plt.ylabel('Evaluation')
plt.xlabel('Generation')
plt.show()
