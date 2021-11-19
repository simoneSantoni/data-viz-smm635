# ! /usr/env/bin python3
# -*-encoding utf-8-*-

"""
--------------------------------------------------------------------------------
    Time series decomposition, part I
--------------------------------------------------------------------------------
Author: Simone Santoni, simone.santoni.1@city.ac.uk;
        credits to https://github.com/selva86
Dates: - created Thu Oct 24 11:06:17 UTC 2019
       - last change
Notes: This script uses Statsmodels for time series decomposition and visualization

"""


# %% libraries
import os
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import statsmodels.api as sm

# %%  matplotlib viz setup
rc('font',**{'family':'serif','serif':['Avant Garde']})
rc('text', usetex=True)

# %% setup
wd = os.getcwd()

# %% read dataset

# source
in_file = os.path.join(wd, 'data', 'airlinePassengers',
                       'airline_passengers.csv')

# df
df = pd.read_csv(in_file)

# data transformation
df.loc[:, 'Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)


# %% decompose data series and plot

# use sm to decompose the series
decomposition = sm.tsa.seasonal_decompose(df['Passengers'], model='additive')

# plot the components of the data series with the plot method
fig = decomposition.plot()

# savefig
out_f = os.path.join(os.getcwd(), 'time_series_decomposition.pdf')
fig.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0)
