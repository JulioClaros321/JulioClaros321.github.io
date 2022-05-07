import matplotlib
matplotlib.use('Agg')

import sys
import os

from matplotlib.testing.decorators import image_comparison

import matplotlib.pylab as plt
import numpy as np

sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path


@image_comparison(baseline_images=['fill1'], extensions=['png'])
def test_fill_between():

    import matplottheme as mpt
    fig = plt.figure()
    ax = fig.add_subplot(111)

    np.random.seed(0)

    x = np.arange(0, 10, 0.01)
    for i in range(8):
        y1 = np.sin(x + i * 0.5)
        y2 = np.sin(x + i * 0.5 + 0.3)

        mpt.fill_between(ax, x, y1, y2)


@image_comparison(baseline_images=['fill2'], extensions=['png'])
def test_fill_betweenx():

    import matplottheme as mpt
    fig = plt.figure()
    ax = fig.add_subplot(111)

    np.random.seed(0)

    y = np.arange(0, 1, 0.01)
    for i in range(8):
        x1 = np.tan(y + i * 0.05)
        x2 = np.tan(y + i * 0.05 + 0.03)

        mpt.fill_betweenx(ax, y, x1, x2)
