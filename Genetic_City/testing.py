import numpy as np
import random
from evaluator import evaluate

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


N = 3
a = np.random.rand(N,N)
b = np.random((N,N+1))
b[:,:-1] = a

print (b)
print (b.sort())
