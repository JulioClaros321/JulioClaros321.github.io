import matplotlib
matplotlib.use('Agg')

import sys, os

from matplotlib.testing.decorators import image_comparison

import matplotlib.pylab as plt
import numpy as np

sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path

@image_comparison(baseline_images=['pcolormesh1'], extensions=['png'])
def test_pcolormesh():
    
    import matplottheme as mpt 
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    np.random.seed(0)

    mpt.pcolormesh(ax, np.random.rand(20, 20) - 0.5, xticks=[str(i) for i in range(20)],
               yticks=[str(i + 20) for i in range(20)])

@image_comparison(baseline_images=['pcolormesh2'], extensions=['png'])
def test_pcolormesh_cold():
    
    import matplottheme as mpt 
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    np.random.seed(0)

    mpt.pcolormesh(ax, np.random.rand(20, 20) - 1, xticks=[str(i) for i in range(20)],
               yticks=[str(i + 20) for i in range(20)])

@image_comparison(baseline_images=['pcolormesh3'], extensions=['png'])
def test_pcolormesh_warm():
    
    import matplottheme as mpt 
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    np.random.seed(0)

    mpt.pcolormesh(ax, np.random.rand(20, 20), xticks=[str(i) for i in range(20)],
               yticks=[str(i + 20) for i in range(20)])

@image_comparison(baseline_images=['pcolormesh4'], extensions=['png'])
def test_pcolormesh_unbalanced():
    
    import matplottheme as mpt 
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    np.random.seed(0)

    mpt.pcolormesh(ax, np.random.rand(20, 20) - 0.4, xticks=[str(i) for i in range(20)],
               yticks=[str(i + 20) for i in range(20)], vmin=-0.6)
