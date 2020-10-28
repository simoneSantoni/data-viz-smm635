# ! /usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    Tufte's slope chart
--------------------------------------------------------------------------------

Author: Simone Santoni, simone.santoni.1@city.ac.uk
        -- credits to https://www.machinelearningplus.com/

Dates: - created Thu Oct 24 11:06:17 UTC 2019
       - last change Thu Oct 24 11:06:17 UTC 2019

Notes: --

"""

# %% load libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# %% read data
url = "https://raw.githubusercontent.com/selva86/datasets/master/gdppercap.csv"
df = pd.read_csv(url)

# %% prepare data
left_label = [str(c) + ', ' + str(round(y))
              for c, y in zip(df.continent, df['1952'])]
right_label = [str(c) + ', ' + str(round(y))
               for c, y in zip(df.continent, df['1957'])]
klass = ['red' if (y1 - y2) < 0 else 'green'
         for y1, y2 in zip(df['1952'], df['1957'])]

# %% draw line

# custom function that defines a new line
def newline(_p_1, _p_2, color='black'):
    _ax = plt.gca()
    _l = mlines.Line2D([_p_1[0], _p_2[0]], [_p_1[1], _p_2[1]],
                       color='orange' if _p_1[1] - _p_2[1] > 0 else 'black',
                       marker='o', markersize=6)
    _ax.add_line(_l)
    return _l

# %% create figure

# create figure
fig = plt.figure(figsize=(14, 14))

# create plot
ax = fig.add_subplot(1, 1, 1)

# add lower and upper bound lines
ax.vlines(x=1, ymin=500, ymax=13000,
          color='black', alpha=0.7,
          linewidth=1, linestyles='dotted')
ax.vlines(x=3, ymin=500, ymax=13000,
          color='black', alpha=0.7,
          linewidth=1, linestyles='dotted')

# add points
ax.scatter(y=df['1952'], x=np.repeat(1, df.shape[0]),
           s=10, color='black', alpha=0.7)
ax.scatter(y=df['1957'], x=np.repeat(3, df.shape[0]),
           s=10, color='black', alpha=0.7)

# line segments and annotations
for p1, p2, c in zip(df['1952'], df['1957'], df['continent']):
    newline([1, p1], [3, p2])
    ax.text(1 - 0.05, p1, c + ', ' + str(round(p1)),
            horizontalalignment='right',
            verticalalignment='center',
            fontdict={'size': 14})
    ax.text(3 + 0.05, p2, c + ', ' + str(round(p2)),
            horizontalalignment='left',
            verticalalignment='center',
            fontdict={'size': 14})

# 'before' and 'after' annotations
ax.text(1 - 0.05, 13000, 'BEFORE',
        horizontalalignment='right',
        verticalalignment='center',
        fontdict={'size': 18, 'weight': 700})
ax.text(3 + 0.05, 13000, 'AFTER',
        horizontalalignment='left',
        verticalalignment='center',
        fontdict={'size': 18, 'weight': 700})

# decoration
ax.set_title("Slopechart: Comparing GDP Per Capita between 1952 vs 1957",
             fontdict={'size': 22})
ax.set(xlim=(0, 4), ylim=(0, 14000), ylabel='Mean GDP Per Capita')
ax.set_xticks([1, 3])
ax.set_xticklabels(["1952", "1957"])
plt.yticks(np.arange(500, 13000, 2000), fontsize=12)

# lighten borders
plt.gca().spines["top"].set_alpha(.0)
plt.gca().spines["bottom"].set_alpha(.0)
plt.gca().spines["right"].set_alpha(.0)
plt.gca().spines["left"].set_alpha(.0)

# save figure
plt.tight_layout()
plt.savefig(os.path.join(os.getcwd(), 'slope_chart.pdf'))

# show plot
plt.show()
