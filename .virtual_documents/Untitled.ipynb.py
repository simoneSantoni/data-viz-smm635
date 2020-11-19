import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


n = np.random.normal(0, 10, 1000)


p = np.random.poisson(10, 1000)


df = pd.DataFrame({'Normal distr.': n, 'Poisson distr.': p})


df


# continuous variable case
sns.displot(df, x='Normal distr.')


# replacing counts with probabilities
sns.displot(df, x='Normal distr.', stat='probability')


# let's get a kernel density
sns.displot(df, x='Normal distr.', kind='kde', bw_adjust=2)


# discrete variable case
sns.displot(df, x='Poisson distr.', discrete=True)


df


molten


# conditioning on a third variable is simple
molten = pd.melt(df, value_name='Score', var_name='Distribution')
sns.displot(molten, x='Score', hue='Distribution', element='step')


# producing a bivariate histogram
sns.displot(df, x='Normal distr.', y='Poisson distr.', kind='kde')


# daw a combo histogram and scatterplot with density contours
# create figure
fig = plt.figure(figsize=(6, 6))
# add plot
ax = fig.add_subplot(111)
# plot data
n0 = np.random.normal(0, 2, 10000)
n1 = np.random.normal(0, 1, 10000)
sns.scatterplot(x=n0, y=n1, s=5, color="gray", ax=ax)
sns.histplot(x=n0, y=n1, bins=50, pthresh=.1, cmap="mako", ax=ax)
sns.kdeplot(x=n0, y=n1, levels=5, color="w", linewidths=1, ax=ax)
# adjust axes
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_ticks_position('right')
ax.xaxis.set_ticks_position('top')
# show plot
plt.show()
