# -*- coding: utf-8 -*-

"""
 ██████╗ ███████╗███╗   ██╗███████╗████████╗██╗ ██████╗     ██████╗██╗████████╗██╗   ██╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝    ██╔════╝██║╚══██╔══╝╚██╗ ██╔╝
██║  ███╗█████╗  ██╔██╗ ██║█████╗     ██║   ██║██║         ██║     ██║   ██║    ╚████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝     ██║   ██║██║         ██║     ██║   ██║     ╚██╔╝
╚██████╔╝███████╗██║ ╚████║███████╗   ██║   ██║╚██████╗    ╚██████╗██║   ██║      ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝     ╚═════╝╚═╝   ╚═╝      ╚═╝

Functions used for selection of best individuals in algorithnm.

By: Andres Rico - aricom@mit.edu
MIT Media Lab - City Science Group
                                                                                      """

import numpy as np
from progressbar import printProgressBar #Import progress bar function.

def match(match_array):
    return np.argmax(match_array)

def select_cities_tournament(city_to_ev, input_city_pop, population, citysize, tournament_size):

    selection_percent = tournament_size

    printProgressBar(0, population, prefix = 'Population Selection Progress:', suffix = 'Complete', length = 50)
    selected_population_matrix = np.zeros((population, citysize*citysize))

    for tournaments in range(0, int(population / selection_percent)):
        winner = match(city_to_ev[int(tournaments*selection_percent):int((tournaments*selection_percent)+selection_percent)])

        champion_replication = []
        for copies in range(0, int(selection_percent)):
            champion_replication.append(input_city_pop[int((tournaments*selection_percent)+winner)])

        selected_population_matrix[int(tournaments*selection_percent):int((tournaments*selection_percent)+selection_percent)] = champion_replication

        printProgressBar(tournaments + 1, population, prefix = 'Population Selection Progress:', suffix = 'Complete', length = 50)
    return selected_population_matrix


def select_cities_rough(city_to_ev, input_city_pop, population, citysize, best_ind, best_ev):

    selected_population_matrix = np.zeros((population, citysize*citysize))
    print('This is the best ev: ', city_to_ev[np.argmax(city_to_ev)])

    if city_to_ev[np.argmax(city_to_ev)] > best_ev:
        best = np.argmax(city_to_ev)
        selected_population_matrix[0:int(population*.5)] = input_city_pop[best]
        city_to_ev[best] = 0

        best = np.argmax(city_to_ev)
        selected_population_matrix[int(population*.5):int(population*.8)] = input_city_pop[best]
        city_to_ev[best] = 0

        best = np.argmax(city_to_ev)
        selected_population_matrix[int(population*.8):int(population)] = input_city_pop[best]
    else:
        selected_population_matrix[0:int(population*.5)] = best_ind

        best = np.argmax(city_to_ev)
        selected_population_matrix[int(population*.5):int(population*.8)] = input_city_pop[best]
        city_to_ev[best] = 0

        best = np.argmax(city_to_ev)
        selected_population_matrix[int(population*.8):int(population)] = input_city_pop[best]

    return selected_population_matrix
