# ! /usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    Lollipop chart
--------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk
        -- credits to https://www.machinelearningplus.com/

Dates: - created 10/27/2020, 11:44:58 PM
       - last change

Notes: --

"""


# %% load libraries
import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc

# %%  matplotlib viz setup
rc('font',**{'family':'serif','serif':['Avant Garde']})
rc('text', usetex=True)

# %% setup
wd = os.getcwd()

# %% read data

# target data file
in_file = os.path.join(wd, 'data', 'movieIndustry', 'lead_actor_race.csv')

# df
df = pd.read_csv(in_file)


# %% viz

# figure
fig = plt.figure(figsize=(6, 4))

# add plot
ax = fig.add_subplot(111)

# plot data
ax.scatter(df['year'], df['minority'], marker='o', color='firebrick',
           edgecolor='w')
ax.vlines(x=df['year'], ymin=0, ymax=df['minority'] - 1, color='firebrick',
          alpha=0.7, linewidth=1)

# text boxes
for row in df.itertuples():
    ax.text(row.year, row.minority+1, s=round(row.minority, 2),
            horizontalalignment= 'center', verticalalignment='bottom')

# axes
ax.axes.get_yaxis().set_visible(False)

# title
plt.title(r'Percentage of minority actors in a leading role')

# hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# save plot
out_f = os.path.join(os.getcwd(), 'lollipop_chart.png')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0,
            dpi=600)

# show plot
plt.show()
