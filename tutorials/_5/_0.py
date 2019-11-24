# ! /usr/env/bin python3
# -*- encoding utf-8 -*-

'''
------------------------------------------------------------------------------
    Counts plot
------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk

Dates:

Notes:

'''


# %% libraries
# ------------

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# %% read data
# ------------

srv = '/Users/simone/'
path = 'PycharmProjects/smm635/tutorials'
fdr = 'data/killerAps'
in_f = 'data.csv'

target = os.path.join(srv, path, fdr, in_f)
df = pd.read_csv(target)


# %% get a preview of daa
# -----------------------

df_counts = df.groupby(['cat', 'killerappgros']).size().reset_index(
    name='counts')


# %% stripplot
# ------------

# create figure
fig = plt.figure(figsize=(9,6))

# create plot
ax = fig.add_subplot(1, 1, 1)

# stripplot
sns.stripplot(df_counts.cat, df_counts.counts,
              size=df_counts.counts*2, ax=ax)

# axes
# ax.set_xlabel(fontsize=12)

# title
plt.title('Counts Plot - Size of circle is bigger as more points overlap',
          fontsize=22)

# show plot
plt.show()
