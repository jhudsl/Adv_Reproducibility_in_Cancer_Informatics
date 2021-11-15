# C. Savonen 2021

import pandas as pd
import numpy as np
import random

# For making a legend
from matplotlib.patches import Patch
import matplotlib.pyplot as plt


def make_color_key(variable):
    """Creates color coding components for a pandas Series variable provided

    Args:
      variable: A pandas Series like metadata['exp_group']

    Returns:
      A dict with two entries:
           'color_key_dict' has the dictionary of what group belongs to what color
           'color_key' has the pandas series variable recoded according to the 'color_key_dict'
    """
    # How many colors do we need?
    num_colors = len(variable.unique())

    # Retrieve this many colors
    colors = [
        "#" + "".join([random.choice("0123456789ABCDEF") for i in range(6)])
        for j in range(num_colors)
    ]

    # Make color key dictionary for these groups
    color_key_dict = dict(zip(variable.unique(), colors))

    # Make into data frame where index is sample IDs
    color_key = pd.Series(variable.map(color_key_dict))

    return {"color_key_dict": color_key_dict, "color_key": color_key}


def make_legend(color_key_dict):
    """Creates color key legend for a dictionary provided

    Args:
      color_key_dict: A dictionary obtained from make_color_key might look like metadata['refinebio_treatment']
    Returns:
      A list that is ready for making a legend out of with plt.legend or heatmap.ax_row_dendrogram.legend or
      heatmap.ax_col_dendrogram.legend
    """

    # Set up based on color dictionary
    handles = [Patch(facecolor=color_key_dict[name]) for name in color_key_dict]

    return handles
