import matplotlib
matplotlib.use('Agg')

import sys, os

from matplotlib.testing.decorators import image_comparison

import matplotlib.pylab as plt
import numpy as np

sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path

@image_comparison(baseline_images=['plot1'], extensions=['png'])
def test_plot_with_legend():
    
    import matplottheme as mpt
    mpt.set_theme('ggplot2', 'ggplot2')    
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    np.random.seed(0)

    for i in range(8):
        y = np.random.normal(size=1000).cumsum()
        x = np.arange(1000)

        mpt.plot(ax, x, y, label='Data {index}'.format(index=str(i + 1)))
    mpt.legend(ax)
    
    mpt.set_theme('default', 'default')   
