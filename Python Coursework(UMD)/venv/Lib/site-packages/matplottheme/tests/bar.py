import matplotlib
matplotlib.use('Agg')

from matplotlib.testing.decorators import image_comparison

import matplotlib.pylab as plt
import matplottheme as mpt
import numpy as np


@image_comparison(baseline_images=['bar1'], extensions=['png'])
def test_two_bar_with_legend():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    np.random.seed(0)

    x = np.arange(6)
    y1 = np.random.uniform(size=6) * 100
    y2 = np.random.uniform(size=6) * 100

    mpt.bar(ax, x, y1, width=0.4, label='Data 1',
            annotations=[str(int(d)) for d in y1])
    mpt.bar(ax, x + 0.4, y2, width=0.4, label='Data 2',
            annotations=[str(int(d)) for d in y2])
    ax.set_xticks(np.arange(6) + 0.4)
    ax.set_xticklabels(
        ['Set {index}'.format(index=str(i)) for i in np.arange(6) + 1])
    mpt.legend(ax)


@image_comparison(baseline_images=['bar2'], extensions=['png'])
def test_stack_bar_with_legend():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    np.random.seed(0)

    x = np.arange(6)
    y1 = -np.random.uniform(size=6) * 50
    y2 = np.random.uniform(size=6) * 50
    y3 = np.random.uniform(size=6) * 50

    mpt.bar(ax, x, y1, label='Data 1', annotations=[str(int(d)) for d in y1],
            annotations_loc='center', orientation='horizontal', grid='True',
            ticks=['Set {index}'.format(index=str(i)) for i in np.arange(6) + 1])
    mpt.bar(ax, x, y2, label='Data 2', annotations=[str(int(d)) for d in y2],
            annotations_loc='in', orientation='horizontal')
    mpt.bar(ax, x, y3, offset=y2, label='Data 3', annotations=[str(int(d)) for d in y2 + y3],
            annotations_loc='out', orientation='horizontal')
    mpt.legend(ax, loc='center right')
