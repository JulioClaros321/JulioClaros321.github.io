import matplotlib
matplotlib.use('Agg')

import sys
import os

from matplotlib.testing.decorators import image_comparison

import matplotlib.pylab as plt
import numpy as np

sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path


@image_comparison(baseline_images=['hist1'], extensions=['png'])
def test_hist_with_legend():

    import matplottheme as mpt
    fig = plt.figure()
    ax = fig.add_subplot(111)

    np.random.seed(0)

    for i in range(8):
        x = np.random.normal(size=1000) + i

        mpt.hist(ax, x, label='Data {index}'.format(index=str(i + 1)))
    mpt.legend(ax, title='Legend')


@image_comparison(baseline_images=['hist2'], extensions=['png'])
def test_horizontal_hist_with_legend():

    import matplottheme as mpt
    fig = plt.figure()
    ax = fig.add_subplot(111)

    np.random.seed(1)

    for i in range(8):
        x = np.random.normal(size=1000) + i

        mpt.hist(ax, x, label='Data {index}'.format(index=str(i + 1)),
                 grid=True, orientation='horizontal')
    mpt.legend(ax, title='Legend')
