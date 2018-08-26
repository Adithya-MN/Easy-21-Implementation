import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns


from environment import *
from monte_carlo import *
from plot import *

num_runs = 10000

value = np.zeros((2,11,22))
counter = np.zeros((2,11,22))

for run in range(num_runs):

    mc = Monte_Carlo_Policy(value, counter)
    mc.policy()
    params = mc.return_params()
    value, counter = params['value'], params['counter']

plot(value,counter)
