import pandas as pd


df = pd.DataFrame({'sectors': ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],
                   'average_roe': [0, 2, 5, 3, 6, 1, 2, 4],
                   'countries': ['uk', 'uk', 'uk', 'uk', 'fr', 'fr', 'fr', 'fr'],
                   'time': [0, 0, 1, 1, 0, 0, 1, 1]})


df


import matplotlib.pyplot as plt


y0 = df.loc[(df['countries'] == 'fr') & (df['sectors'] == 'a'), 'average_roe']
y1 = df.loc[(df['countries'] == 'fr') & (df['sectors'] == 'b'), 'average_roe']
y2 = df.loc[(df['countries'] == 'uk') & (df['sectors'] == 'a'), 'average_roe']
y3 = df.loc[(df['countries'] == 'uk') & (df['sectors'] == 'b'), 'average_roe']


fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)

x = [0, 1]
ax.plot(x, y0, c='r')
ax.plot(x, y1, c='g')
ax.plot(x, y2, c='k')
ax.plot(x, y3, c='b')
plt.show()
