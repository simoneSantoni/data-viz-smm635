import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import statsmodels.api as sm
import statsmodels.formula as smf
import pandas as pd


rc('font',**{'family':'serif','serif':['Avant Garde']})
rc('text', usetex=True)


# sample size
num_samples = 1000

# variables' mean 
mu = np.repeat(0, 4)

# names
names = ['job_sat', 'int_qui', 'age', 'org_tnr']


# the desired covariance matrix.
r = np.array([
        [  1.00, -0.40, -0.03,  0.11],
        [ -0.40,  1.00, -0.05, -0.09],
        [ -0.03, -0.05,  1.00,  0.05],
        [  0.11, -0.09,  0.05,  1.00]
    ])

# generate the random samples.
df_1_5 = pd.DataFrame(np.random.multivariate_normal(mu, r, size=num_samples),
                      columns=names)

# expand
df_1_5.loc[:, 'cohort'] = 'micro'
df_1_5.loc[:, 'firm_size'] = np.random.randint(low=1, high=5, size=num_samples)


df_1_5.head()


# the desired covariance matrix.
r = np.array([
        [  1.00, -0.30, -0.03,  0.11],
        [ -0.30,  1.00, -0.05, -0.09],
        [ -0.03, -0.05,  1.00,  0.05],
        [  0.11, -0.09,  0.05,  1.00]
    ])

# generate the random samples.
df_6_25 = pd.DataFrame(np.random.multivariate_normal(mu, r, size=num_samples),
                       columns=names)

# expand
df_6_25.loc[:, 'cohort'] = 'large'
df_6_25.loc[:, 'firm_size'] = np.random.randint(low=6,
                                                high=25,
                                                size=num_samples)


df_6_25.head()


# the desired covariance matrix.
r = np.array([
        [  1.00, -0.25, -0.03,  0.11],
        [ -0.25,  1.00, -0.05, -0.09],
        [ -0.03, -0.05,  1.00,  0.05],
        [  0.11, -0.09,  0.05,  1.00]
    ])

# generate the random samples.
df_26_100 = pd.DataFrame(np.random.multivariate_normal(mu, r, size=num_samples),
                         columns=names)

# expand
df_26_100.loc[:, 'cohort'] = 'medium'
df_26_100.loc[:, 'firm_size'] = np.random.randint(low=26,
                                                  high=100,
                                                  size=num_samples)


# the desired covariance matrix.
r = np.array([
        [  1.00, -0.20, -0.03,  0.11],
        [ -0.20,  1.00, -0.05, -0.09],
        [ -0.03, -0.05,  1.00,  0.05],
        [  0.11, -0.09,  0.05,  1.00]
    ])

# generate the random samples.
df_101_500 = pd.DataFrame(np.random.multivariate_normal(mu, r, size=num_samples),
                          columns=names)

# expand
df_101_500.loc[:, 'cohort'] = 'large'
df_501_.loc[:, 'firm_size'] = np.random.randint(low=101, high=500,
                                                size=num_samples)


# the desired covariance matrix.
r = np.array([
        [  1.00, -0.15, -0.03,  0.11],
        [ -0.15,  1.00, -0.05, -0.09],
        [ -0.03, -0.05,  1.00,  0.05],
        [  0.11, -0.09,  0.05,  1.00]
    ])

# generate the random samples.
df_501_ = pd.DataFrame(np.random.multivariate_normal(mu, r, size=num_samples),
                       columns=names)

# expand
df_501_.loc[:, 'cohort'] = 'very large'
df_501_.loc[:, 'firm_size'] = np.random.randint(low=501, high=2000,
                                                size=num_samples)


df = pd.concat([df_1_5, df_6_25, df_26_100, df_101_500, df_501_],
               axis=0)
df.info()

df.head()






