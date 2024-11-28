# ! /usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    Stacked histogram
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk;
        credits to https://github.com/selva86
Dates: - created Thu Oct 24 11:06:17 UTC 2019
       - last change Thu Oct 24 11:06:17 UTC 2019
Notes: This script produces a histogram that shows the distribution of a
       focal variable conditionally on one or multiple categorical variables
"""


# %% libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

# %%  matplotlib viz setup
plt.style.use('seaborn-bright')
rc('font',**{'family':'sans-serif','sans-serif':['Avant Garde']})
rc('text', usetex=True)

# %% fake data
'''
Simulate three random variables drawn from different distributions
'''
# contoinuous vars
x = np.random.normal(loc=-1, scale=0.75, size=1000)
y = np.random.normal(loc=0, scale=1, size=1000)
z = np.random.normal(loc=1, scale=0.5, size=1000)

# qualitative categories
categories = ['x', 'y', 'z']

np.shape(x)

# %% create figure

# figure
fig = plt.figure(figsize=(6, 4))

# add figure
ax = fig.add_subplot(1, 1, 1)

# plot data
ax.hist([x, y, z], bins=50, histtype="barstacked", density=True,
         label=categories, color=["darkorange", "darkorchid", "lime"],
         alpha=0.6)

# axes
ax.set_xlabel("Values")
ax.set_ylabel("Density")

# legend
ax.legend(loc="best")

# save plot
out_f = os.path.join(os.getcwd(), 'stacked_histogram.pdf')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0)

# show plot
plt.show()
