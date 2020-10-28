# ! /usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    Tufte's line chart
--------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk
        -- credits to https://www.machinelearningplus.com/

Dates: - created 10/27/2020, 11:44:58 PM
       - last change 

Notes: --

"""

# %%  libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# %%  matplotlib viz setup
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)

# %% setup
wd = os.getcwd()

# %% load dataset

# file to source
in_file = os.path.join(wd, 'data', 'movieIndustry', 'lead_actor_race.csv')

# read data
years, n, perc = [], [], []
with open(in_file, 'r') as pipe:
    for line in pipe.readlines()[1:]:
        parsed = line.split(',')
        years.append(int(parsed[0]))
        n.append(int(parsed[1]))
        perc.append(float(parsed[2].strip()))

# %% viz

# create figure
fig = plt.figure(figsize=(6, 4))

# add plot
ax = fig.add_subplot(111)

# populate plot
ax.plot(years, n, marker='o', color='k', markersize=6, markerfacecolor='k',
        markeredgecolor='w', markeredgewidth=2)

# hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

#  axes
ax.set_xlabel('Year')
ax.set_xticks(years)
labels = []
for i in years:
    if i % 2 !=0:
        labels.append(str(i))
    else:
        labels.append('')
ax.set_xticklabels(labels, rotation=90)
ax.set_ylabel('Counts of minority artists\nin leading roles')

# secondary axis
axr = ax.twinx()
axr.plot(years, perc, marker='o', color='grey', markersize=6,
         markerfacecolor='grey', markeredgecolor='white', markeredgewidth=2)

# hide the right and top spines
axr.spines['right'].set_visible(False)
axr.spines['top'].set_visible(False)
axr.spines['bottom'].set_visible(False)
axr.spines['left'].set_visible(False)

# axes
axr.set_ylabel('Percentage of minority artists\nin leading roles')

# save plot to file
out_f = os.path.join(os.getcwd(), 'tufte_linechart.png')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0,
            dpi=600)

# show plot
plt.show()
