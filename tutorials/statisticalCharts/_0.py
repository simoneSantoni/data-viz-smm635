# !/usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    Tufte's bar chart
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk
Dates: - created Thu Oct 24 11:06:17 UTC 2019
       - last change Thu Oct 24 11:06:17 UTC 2019
Notes: This script reproduces the bar chart reported in Tufte's book
       "The Display of Quantitative Information" (page 133). For sake of
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
categories = ['A', 'B', 'C', 'D']
counts = [4, 2, 6, 8]

# %% visualization

# data series
pos = np.arange(0, len(categories), 1)

# figure framework
fig = plt.figure(figsize=(5, 3), frameon=True)
ax = fig.add_subplot(1, 1, 1)

# plot data
ax.bar(pos, counts, color='gray', edgecolor='white')

# axes properties
ax.set_xticks(pos)
ax.set_xticklabels(categories, rotation='vertical')
#ax.set_xlabel('Publication year')
#ax.set_ylabel('Counts of studies')
#ax.set_ylabel('Counts of articles')

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
out_f = os.path.join(os.getcwd(), 'tufte_barchart.png')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0,
            dpi=600)

# show plot
plt.show()
