import numpy as np
from progressbar import printProgressBar #Import progress bar function.

#Function creates a random city design by assigning a specific number to each block.
#Number key is based on the block representation used on the Bento Scope.
def citygen(desired_size):
    city = np.round(np.random.rand(desired_size,desired_size)*9) #Random matrix of specified size with numbers between 0 - 9.
    for x in range(0, desired_size):
        for y in range(0 , desired_size):
            if (city[x][y]) == 0: #Change all the zeros into ones.
                city[x][y] = 1
    city = np.reshape(city, desired_size * desired_size) #Reshapes matrix into a single vector for better management.
    return (city)

#Function creates a matrix with a specific number of cities and size.
#Number of cities is the total population of cities for the algorithm.
def create_cities(cities, size):
    printProgressBar(0, cities, prefix = 'Population Generation Progress:', suffix = 'Complete', length = 50) #Progress bar for terminal interface.
    matrix = np.arange(citysize * citysize) #Creates empty vector to be used to create matrix.
    for indiv in range(0, cities):
        newcity = citygen(citysize) #Calls new city generator.
        matrix = np.vstack((matrix, newcity)) #Adds new city to complete population matrix.
        printProgressBar(indiv + 1, cities, prefix = 'Population Generation Progress:', suffix = 'Complete', length = 50) #Progress bar for terminal interface.
    matrix = np.delete(matrix, 0, 0) #Deletes fisrt row used as placeholder.
    return matrix #Returns matrix with each row representing a different city.
