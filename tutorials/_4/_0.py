# ! /usr/env/bin python3
# -*- encoding utf-8 -*-

'''
------------------------------------------------------------------------------
    Counts plot
------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk

<<<<<<< HEAD
Dates: - created 5/11/2019 12:50:35
       - last change 25/11/2019 00:50:35

Notes: --
=======
Dates:

Notes:
>>>>>>> origin/master

'''


# %% libraries
# ------------

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# %% read data
# ------------

<<<<<<< HEAD
dr = os.getcwd()
fdr = 'data/killerAps'
in_f = 'data.csv'

target = os.path.join(dr, fdr, in_f)
=======
srv = '/Users/simone/'
path = 'PycharmProjects/smm635/tutorials'
fdr = 'data/killerAps'
in_f = 'data.csv'

target = os.path.join(srv, path, fdr, in_f)
>>>>>>> origin/master
df = pd.read_csv(target)


# %% get a preview of daa
# -----------------------

<<<<<<< HEAD
gr = df.groupby(['cat', 'killerappgros'])
df_counts = gr.size().reset_index(name='counts')
=======
df_counts = df.groupby(['cat', 'killerappgros']).size().reset_index(
    name='counts')
>>>>>>> origin/master


# %% stripplot
# ------------

# create figure
<<<<<<< HEAD
fig = plt.figure(figsize=(6, 4))
=======
fig = plt.figure(figsize=(9,6))
>>>>>>> origin/master

# create plot
ax = fig.add_subplot(1, 1, 1)

# stripplot
<<<<<<< HEAD
sns.stripplot(df_counts.cat, df_counts.counts, hue=df_counts.killerappgros,
              data=df_counts, ax=ax)

# axes
ax.set_xlabel('Category of app in the AppStore')
ax.set_yscale('log')
ax.set_ylabel('Count of apps')

# title
plt.title('Counts Plot - Size of circle is bigger as more points overlap')

# legend
ax.legend(loc='best')

# save plot
plt.tight_layout()
plt.savefig('counts_plot.pdf')
=======
sns.stripplot(df_counts.cat, df_counts.counts,
              size=df_counts.counts*2, ax=ax)

# axes
# ax.set_xlabel(fontsize=12)

# title
plt.title('Counts Plot - Size of circle is bigger as more points overlap',
          fontsize=22)
>>>>>>> origin/master

# show plot
plt.show()
