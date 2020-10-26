#!/usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    Stacked bar chart
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk;
        credits to https://github.com/selva86
Dates: - created Thu Oct 24 11:06:17 UTC 2019
       - last change Thu Oct 24 11:06:17 UTC 2019
Notes: This script produces a barchart that shows the distribution of a
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
teams = ['A', 'B', 'C', 'D', 'E']
work_from_home = [20, 35, 30, 35, 27]
in_office = [25, 32, 34, 20, 25]
work_from_home_std = [2, 3, 4, 1, 2]
in_office_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

# %% stacked barchart

# create figure
fig = plt.figure(figsize=(6, 4))

# create plot
ax = fig.add_subplot(1, 1, 1)

# plot data
ax.bar(teams, work_from_home, width, yerr=work_from_home_std,
       label='Employees working\nfrom home', color='white', edgecolor='k')
ax.bar(teams, in_office, width, yerr=in_office_std, bottom=work_from_home,
       label='Employees working\nfrom office', color='lightgrey',
       edgecolor='k')

# axes
ax.set_ylabel('Scores')
ax.set_title('Scores by team and policy')
ax.legend()

# legend
ax.legend(loc='best')

# save plot
out_f = os.path.join(os.getcwd(), 'stacked_barchart.pdf')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0)

# show plot
plt.show()
