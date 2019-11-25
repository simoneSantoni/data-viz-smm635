
# ! /usr/env/bin python3
# -*- encoding utf-8 -*-

'''
------------------------------------------------------------------------------
    Counts plot
------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk

Dates: - created 5/11/2019 12:50:35
       - last change 25/11/2019 00:50:35

Notes: --
=======
Dates:

Notes:

'''


# %% load libraries
# -----------------

import os
import pandas as pd
import matplotlib.pyplot as plt


# %% prepare data
# ---------------

df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
x = df.loc[:, ['mpg']]
df['mpg_z'] = (x - x.mean())/x.std()
df['colors'] = ['red' if x < 0 else 'darkgreen' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)


# %% draw plot
# ------------

# create plot
fig = plt.figure(figsize=(14,16), dpi= 80)

# create plot
ax = fig.add_subplot(1, 1, 1)

# scatter
ax.scatter(df.mpg_z, df.index, s=450, alpha=.6, color=df.colors)

for x, y, label in zip(df.mpg_z, df.index, df.mpg_z):
    t = plt.text(x, y, round(label, 1), horizontalalignment='center',
                 verticalalignment='center', fontdict={'color':'white'})

# Decorations
# Lighten borders
plt.gca().spines["top"].set_alpha(.3)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(.3)
plt.gca().spines["left"].set_alpha(.3)

# axes
plt.yticks(df.index, df.cars)
plt.title('Diverging Dotplot of Car Mileage', fontdict={'size':20})
plt.xlabel('$Mileage$')

# grid
plt.grid(linestyle='--', alpha=0.5)
plt.xlim(-2.5, 2.5)

# save plot
plt.tight_layout()
plt.savefig(os.path.join(os.getcwd(), 'diverging_plot_0.pdf'))

# show plot
plt.show()