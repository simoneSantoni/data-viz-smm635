# ! /usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    Scattered histogram
--------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk;
        credits to https://github.com/selva86

Dates: - created Thu Oct 24 11:06:17 UTC 2019
       - last change Thu Oct 24 11:06:17 UTC 2019

Notes: This script produces a histogram that shows the distribution of a
       focal variable 'x' conditionally on a categorical variables 'z'

"""


# %% libraries
# ------------

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# %% read data
# ------------

target = "https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv"
df = pd.read_csv(target)


# %% data preparation
# -------------------

x_var = 'displ'
groupby_var = 'class'
df_agg = df.loc[:, [x_var, groupby_var]].groupby(groupby_var)
vals = [df[x_var].values.tolist() for i, df in df_agg]


# %% create figure
# ----------------

# figure
fig = plt.figure(figsize=(9, 6))

# add figure
ax = fig.add_subplot(1, 1, 1)

# colormap
colors = [plt.cm.Spectral(i/float(len(vals)-1)) for i in range(len(vals))]
n, bins, patches = ax.hist(vals, 30, stacked=True, density=False,
                           color=colors[:len(vals)])

# legend
plt.legend({group:col for group, col in
            zip(np.unique(df[groupby_var]).tolist(), colors[:len(vals)])})

# title
plt.title(f"Stacked Histogram of ${x_var}$ colored by ${groupby_var}$",
          fontsize=22)

# axes
plt.xlabel(x_var)
plt.ylabel("Frequency")
plt.ylim(0, 25)
plt.xticks(ticks=bins[::3], labels=[round(b,1) for b in bins[::3]])

# save plot
out_f = os.path.join(os.getcwd(), 'stacked_histogram.pdf')
fig.savefig(out_f)

# show plot
plt.show()
