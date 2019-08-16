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

def match(participant_1, participant_2, participant_3, participant_4):
    match_array = [participant_1, participant_2, participant_3, participant_4]
    return np.argmax(match_array)

def select_cities(city_to_ev, input_city_pop, population, citysize):

    printProgressBar(0, population, prefix = 'Population Selection Progress:', suffix = 'Complete', length = 50)
    selected_population_matrix = np.zeros((population, citysize*citysize))

    for tournaments in range(0, population):
        if tournaments >= (population - 3):
            if tournaments == population - 3:
                winner = match(city_to_ev[0], city_to_ev[tournaments], city_to_ev[tournaments + 1], city_to_ev[tournaments + 2] )
            if tournaments == population - 2:
                winner = match(city_to_ev[0], city_to_ev[1], city_to_ev[tournaments], city_to_ev[tournaments + 1] )
            if tournaments == population - 1:
                winner = match(city_to_ev[0], city_to_ev[1], city_to_ev[2], city_to_ev[tournaments] )

            if winner == 0:
                selected_population_matrix[tournaments,:] = input_city_pop[0]
            if winner == 1:
                selected_population_matrix[tournaments,:] = input_city_pop[tournaments]
            if winner == 2:
                selected_population_matrix[tournaments,:] = input_city_pop[0]
            if winner == 3:
                selected_population_matrix[tournaments,:] = input_city_pop[tournaments]

        else:
            winner = match(city_to_ev[tournaments], city_to_ev[tournaments + 1], city_to_ev[tournaments + 2], city_to_ev[tournaments + 3])
            if winner == 0:
                selected_population_matrix[tournaments,:] = input_city_pop[tournaments]
            if winner == 1:
                selected_population_matrix[tournaments,:] = input_city_pop[tournaments + 1]
            if winner == 2:
                selected_population_matrix[tournaments,:] = input_city_pop[tournaments + 2]
            if winner == 3:
                selected_population_matrix[tournaments,:] = input_city_pop[tournaments + 3]

        printProgressBar(tournaments + 1, population, prefix = 'Population Selection Progress:', suffix = 'Complete', length = 50)
        return selected_population_matrix
