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
'''


# %% libraries
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# %% read data
wd = os.getcwd()
fdr = 'data/killerAppData'
in_f = 'data.csv'
df = pd.read_csv(os.path.join(wd, fdr, in_f))

# %% get a preview of data
gr = df.groupby(['cat', 'killerappgros'])
df_counts = gr.size().reset_index(name='counts')

# %% stripplot

# create figure
fig = plt.figure(figsize=(6, 4))

# create plot
ax = fig.add_subplot(1, 1, 1)

# stripplot
sns.stripplot(df_counts['cat'],
              df_counts['counts'],
              hue=df_counts['killerappgros'],
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

# save plot
plt.tight_layout()
plt.savefig(os.path.join(os.getcwd(), 'count_plot.pdf'))

# show plot
plt.show()

# %%
