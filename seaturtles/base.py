import subprocess
import shutil
import json
import pandas as pd
import h5py
import numpy as np
from scipy.interpolate import interp1d
import utm
import os
import matplotlib.pyplot as plt

# set all single line variables to be displayed, not just the last line
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

from IPython.display import display

## get the absolute path name of the included EQHazard.jar file
import seaturtles
import inspect
EQHazard_file = os.path.dirname(inspect.getfile(seaturtles)) + '\EQHazard.jar'

def set_plot_formatting():
    # set up plot formatting
    SMALL_SIZE = 15
    MEDIUM_SIZE = 18
    BIGGER_SIZE = 25

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=MEDIUM_SIZE)    # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
