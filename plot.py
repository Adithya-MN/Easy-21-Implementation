import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from monte_carlo import *

def plot(value, counter):

    value_max = np.amax(value, axis = 2)

    fig = plt.figure()

    _plot = fig.add_subplot(111, projection = '3d')
    x = range(1,11)
    y = range(1,22)
    X, Y = np.meshgrid(x,y)

    _plot.plot_wireframe(X, Y, value_max)
    _plot.set_ylabel('Player sum')
    _plot.set_xlabel('Dealer_card')
    _plot.set_zlabel('Value Function')

    _plot.show()
