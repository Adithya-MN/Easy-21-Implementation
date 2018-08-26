import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def _plot(value, counter):

    value_max = np.amax(value, axis = 2)

    fig = plt.figure()

    _plot_ = fig.add_subplot(111, projection = '3d')
    x = range(1,11)
    y = range(1,22)
    X, Y = np.meshgrid(x,y)


    _plot_.plot_wireframe(X, Y, value_max.T)
    _plot_.set_ylabel('Player sum')
    _plot_.set_xlabel('Dealer_card')
    _plot_.set_zlabel('Value Function')

    _plot_.show()
