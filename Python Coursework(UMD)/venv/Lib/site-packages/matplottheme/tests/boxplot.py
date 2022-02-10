import matplotlib
matplotlib.use('Agg')

from matplotlib.testing.decorators import image_comparison

import matplotlib.pylab as plt
import matplottheme as mpt
import numpy as np


@image_comparison(baseline_images=['boxplot1'], extensions=['png'])
def test_box():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    np.random.seed(0)

    x = np.random.normal(size=(1000, 8))

    mpt.boxplot(
        ax, x, ticks=['Set {index}'.format(index=i + 1) for i in range(8)])


@image_comparison(baseline_images=['boxplot2'], extensions=['png'])
def test_horizontal_box():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    np.random.seed(0)

    x = np.random.normal(size=(1000, 8))

    mpt.boxplot(
        ax, x, vert=False, ticks=['Set {index}'.format(index=i + 1) for i in range(8)])
