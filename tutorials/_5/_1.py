# ! /usr/env/bin python3
# -*- encoding utf-8 -*-

'''
------------------------------------------------------------------------------
    Diverging plot with annotations
------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk

Dates: - created 5/11/2019 12:50:35
       - last change 25/11/2019 00:50:35

Notes: --

'''


# %% load libraries
# -----------------

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# %% load and prepare data
# ------------------------

# read data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")

# slice
x = df.loc[:, ['mpg']]

# z-scores
df['mpg_z'] = (x - x.mean())/x.std()
df['colors'] = 'black'

# color fiat differently
df.loc[df.cars == 'Fiat X1-9', 'colors'] = 'darkorange'
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)


# %% plot data

# create figure
fig = plt.figure(figsize=(14,16), dpi= 80)

# create plot
ax = fig.add_subplot(1, 1, 1)

# horizontal lines
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z,
           color=df.colors, alpha=0.4, linewidth=1)
plt.scatter(df.mpg_z, df.index,
            color=df.colors,
            s=[600 if x == 'Fiat X1-9' else 300 for x in df.cars], alpha=0.6)
plt.yticks(df.index, df.cars)
plt.xticks(fontsize=12)

# annotations
plt.annotate('Mercedes Models',
             xy=(0.0, 11.0), xytext=(1.0, 11), xycoords='data',
             fontsize=15, ha='center', va='center',
             bbox=dict(boxstyle='square', fc='firebrick'),
             arrowprops=dict(arrowstyle='-[, widthB=2.0, lengthB=1.5',
                            lw=2.0, color='steelblue'), color='white')

# patches
p1 = patches.Rectangle((-2.0, -1), width=.3, height=3, alpha=.2, facecolor='red')
p2 = patches.Rectangle((1.5, 27), width=.8, height=5, alpha=.2, facecolor='green')
plt.gca().add_patch(p1)
plt.gca().add_patch(p2)

# decorate
plt.title('Diverging Bars of Car Mileage', fontdict={'size':20})
plt.grid(linestyle='--', alpha=0.5)

# save plot
plt.tight_layout()
plt.savefig(os.path.join(os.getcwd(), 'diverging_plot_1.pdf'))


# show plot
plt.show()