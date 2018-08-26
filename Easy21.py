import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns


from environment import *
from monte_carlo import *
from plot import *

num_runs = 10000

value = np.zeros((10,21,2))
counter = np.zeros((10,21,2))

for run in range(num_runs):

    if(run == 0):
        mc = Monte_Carlo_Policy(value, counter, True)
    else:
        mc = Monte_Carlo_Policy(value, counter, False)
    mc.policy()
    params = mc.return_params()
    value, counter = params['value'], params['counter']

plot(value,counter)
