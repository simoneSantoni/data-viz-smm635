
# ! /usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    Stacked area chart
--------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk
        -- credits to https://www.machinelearningplus.com/

Dates: - created 10/28/2020, 12:08:38 AM
       - last change --

Notes: --

"""

# %% load libraries
import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc

# %%  matplotlib viz setup
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)

# %% setup
wd = os.getcwd()

# %% read data

# target data file
in_file = os.path.join(wd, 'data', 'movieIndustry', 'lead_actor_race.csv')

# df
df = pd.read_csv(in_file)

# data series
df.loc[:, 'white'] = 100 - df['minority']

# %% viz

# create viz
fig = plt.figure(figsize=(6, 4))

# add plot
ax = fig.add_subplot(111)

# plot data
ax.fill_between(df['year'], y1=df['minority'], y2=0, label='Minority',
                alpha=0.25, color='r', linewidth=2)
ax.fill_between(df['year'], y1=df['minority'], y2=100, label='White',
                alpha=0.25, color='b', linewidth=2)

# lighten borders
ax.spines["top"].set_alpha(0)
ax.spines["bottom"].set_alpha(.3)
ax.spines["right"].set_alpha(0)
ax.spines["left"].set_alpha(.3)

# labels
ax.set_ylabel('Percentage of leading roles')

# legend
ax.legend(loc='best')

# save plot
out_f = os.path.join(os.getcwd(), 'stacked_area.pdf')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0,
            dpi=600)

# show plot
plt.show()
