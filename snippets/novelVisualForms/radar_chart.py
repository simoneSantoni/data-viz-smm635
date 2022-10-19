# !/usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    radar_chart.py  |  radar chart
--------------------------------------------------------------------------------
Author : Simone Santoni, simone.santoni.1@city.ac.uk

Edits  : created 11/27/2020, 9:18:14 AM; never revised

Notes  : this script shows how to compare and contrast data on careers using
         a relatively novel visual form such as the radar chart

"""

# %% Libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from matplotlib import rc

# %%  matplotlib viz setup
"""
uncomment if you want to render the data viz with TeX
"""
# rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
# rc('text', usetex=True)

# %% data for the chart
# read data
# --+ path to file
in_file = os.path.join('.', 'data', 'nba', 'goat.csv')
# --+ get a df
df = pd.read_csv(in_file)
# player set
players = df.player.unique().tolist()
# get cumulative nba titles
gr = df.groupby('player')
df.loc[:, 'nba_champion'] = gr['nba_champion'].transform(np.cumsum)
# manipulate data
# --+ create career spells with equal length to improve comparability among
#     players
max_expr = np.max(df['sort'])
expr = []
for i in np.arange(1, max_expr + 1):
    for j in players:
        expr.append([i, j])
expr = pd.DataFrame(expr, columns=['sort', 'player'])
df = pd.merge(df, expr, on=['player', 'sort'], how='right')
# we want to radar charts, one for the average points per game, one for the
#     count of titles
variables = ['points', 'nba_champion']
# replace missing values with 0 if player j is inactive in perio j
for variable in variables:
    df.loc[df[variable].isnull(), variable] = 0

# %% visualization
# colors to associate with each player
colors = dict(zip(players, ['orange', 'gray', 'black', 'green']))
# labels for the axes
labels = [i + 1 for i in range(max_expr)]
# create the figure
fig = plt.figure(figsize=(9, 5.5))
# create axes/segments of the chart (we divide the plot into seasons)
angles = [n / float(max_expr) * 2 * pi for n in range(max_expr)]
angles += angles[:1]
# create two plots with ploar axes (plot #1 contains point per game; plot #2
#     contains nba titles)
ax0 = fig.add_subplot(1, 2, 1, polar=True)
ax1 = fig.add_subplot(1, 2, 2, polar=True)
# average points per game chart
# --+ title
ax0.set_title(r'Average point per game by season', pad=20)
# --+ axes
ax0.set_theta_offset(pi / 2)
ax0.set_theta_direction(-1)
# --+ axes and ticks
ax0.set_xticks(angles[:-1])
ax0.set_xticklabels(labels)
# --+ draw ylabels
ax0.set_rlabel_position(0)
#ax0.set_yticks([])
ax1.set_xticklabels(labels)
# plot the data series
for player in players:
    values = df.loc[df['player'] == player, 'points'].tolist()
    values += values[:1]
    ax0.scatter(angles, values, linewidth=1, linestyle='solid',
                label=player, color=colors[player])
#    ax0.fill(angles, values, color=colors[player], alpha=0.1)
# nba titles
# --+ title
ax1.set_title(r'Cumulative count of NBA titles by season', pad=20)
ax1.set_theta_offset(pi / 2)
ax1.set_theta_direction(-1)
# --+ axes and ticks
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(labels)
#ax1.set_yticks([])
ax1.yaxis.label.set_color('white')
# --+ draw ylabels
ax1.set_rlabel_position(0)
# plot the data series
for player in players:
    values = df.loc[df['player'] == player, 'nba_champion'].tolist()
    values += values[:1]
    ax1.plot(angles, values, linewidth=1, linestyle='solid',
             label=player, color=colors[player])
    ax1.fill(angles, values, color=colors[player], alpha=0.1)
# legend
plt.legend(loc='upper right', bbox_to_anchor=(0.21, 0))
# title
plt.suptitle(r'Different pathways to greatness', fontsize=18)
# save plot to file
out_f = os.path.join(os.getcwd(), 'radar_chart.pdf')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0)
# show plot
#plt.show()

# %%
