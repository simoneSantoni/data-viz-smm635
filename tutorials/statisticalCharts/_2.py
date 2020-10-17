# !/usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    Tufte's boxplot chart
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Dates: - created Thu Oct 24 11:06:17 UTC 2019
       - last change Thu Oct 24 11:06:17 UTC 2019
Notes: This script reproduces the box plot reported in Tufte's book
       "The Display of Quantitative Information" (page 125). For sake of
       convenience, I use simulated data.
"""

# %%  libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# %%  matplotlib viz setup
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)

# %% fake data
x = np.random.normal(loc=1, scale=1.2, size=100)
y = np.random.normal(loc=1.5, scale=0.75, size=100)
z = np.random.normal(loc=0.5, scale=0.25, size=100)

# %% visualization

# data series
pos = [1, 2, 3]
vars = ['X', 'Y', 'Z']
mu = [np.mean(a) for a in [x, y, z]]

# artists
flierprops = dict(marker='o',
                  markerfacecolor='w',
                  markeredgecolor='k',
                  markersize=3,
                  linestyle='none')
medianprops = dict(linewidth=0)

# figure framework
fig = plt.figure(figsize=(4, 3), frameon=True)
ax = fig.add_subplot(1, 1, 1)

# plot data
ax.boxplot([x, y, z],
           positions=pos,
           labels=vars,
           meanline=False,
           showbox=False,
           showcaps=False,
           medianprops=medianprops,
           flierprops=flierprops)
ax.scatter(pos, mu, marker='o', s=15, color='black')

# hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

# grid
ax.grid(True, axis='y', ls=':', color='white')

# save plot to file
out_f = os.path.join(os.getcwd(), 'tufte_boxplot.pdf')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0)

# show plot
# plt.show()
