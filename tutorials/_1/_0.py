# ! /usr/env/bin python3
# -*- encoding utf-8 -*-

'''
-------------------------------------------------------------------------------
    Multi-plot figure
-------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk

Dates: last change Fri Nov  1 00:06:33 UTC 2019

Notes: This script produces a multi-plot figure. Plots ara arranged over
       the figure such that to have 2 plots at the top and 1 plot that is
       located in the bottom-center part of the figure.
'''

# %% load libraries
# -----------------

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# %% aesthetics
# -------------

plt.style.use('seaborn-bright')
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=10)


# %% generate fake data
# ---------------------

x = np.arange(0, 10, 1)
y0 = np.square(x)
y1 = np.sqrt(x)
y2 = 2 + x


# %% figure
# ---------

# create figure
fig = plt.figure(figsize=(6, 6))

# parition the figure into 4 subplots with 'gridspec'
gs = gridspec.GridSpec(2, 4, # we want 2 rows, 4 cols
                       figure=fig, # this gs applies to figure
                       hspace=0.5, wspace=1, # separation between plots
                       width_ratios=[1, 1, 1, 1], # ration between the
                       # first and second column
                       height_ratios=[1, 1]) # ration between the first ans second row

# add plots
ax0 = fig.add_subplot(gs[0, 0:2]) # this will occupy the first row-first colum
ax1 = fig.add_subplot(gs[0, 2:4]) # and so on and so forth...
ax2 = fig.add_subplot(gs[1, 1:3])

# plot left-top
ax0.plot(x, y0, marker='o', color='green')
ax0.set_xlabel(r'$x$')
ax0.set_ylabel(r'$x^{2}$')
ax0.grid(ls='--')

# plot right-top
ax1.plot(x, y1, marker='s', color='red')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$\sqrt{x}$')
ax1.grid(ls='--')

# plot middle-bottom
ax2.plot(x, y2, marker='d', color='blue')
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$2 + x$')
ax2.grid(ls='--')

# save plot
out_f = os.path.join(os.getcwd(), 'multiple_plots.pdf')
fig.savefig(out_f)

# show plot
plt.show()