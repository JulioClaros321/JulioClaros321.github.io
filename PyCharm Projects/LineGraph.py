# Julio Claros
# 114153234
# 2018-22-10
# Exercise
"""
Functions that make scatter and line plots using plt.show function
"""


def line_graph():
    """
    Function creates a line via the values place in linespace().

    Returns:
        A line plot
    """
    fig = plt.figure()
    ax = plt.axes()
    x = [1, 2, 3]
    y = [5, 6, 7]
    plt.plot(x, y)
    plt.show()


def make_scatter():
    """
    Function creates a scatter plot via the values place in linespace()

    Returns:
        A scatter plot
    """
    x = np.linspace(4, 8, 6)
    y = np.sin(x)
    plt.plot(x, y, 'o', color='black');
    plt.show()


if __name__ == '__main__':
    %matlablib notebook
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-whitegrid')
    import numpy as np
    line_graph()
    make_scatter()
