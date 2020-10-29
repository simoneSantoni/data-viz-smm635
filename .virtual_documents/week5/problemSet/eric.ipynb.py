import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import matplotlib
warnings.filterwarnings("ignore",category=UserWarning)


#import data sets
jan = pd.read_csv("Jan.csv")
feb = pd.read_csv("Feb.csv")
mar = pd.read_csv("Mar.csv")
apr = pd.read_csv("apr.csv")
may = pd.read_csv("May.csv")
june = pd.read_csv("June.csv")


#specify the data for np.count
jan.data = jan["callsign"]
feb.data = feb["callsign"]
mar.data = mar["callsign"]
apr.data = apr["callsign"]
may.data = may["callsign"]
june.data = june["callsign"]

#creat an array of total number of flights for each month
jan1 = np.count_nonzero(jan.data)
feb1 = np.count_nonzero(feb.data)
mar1= np.count_nonzero(mar.data)
apr1 = np.count_nonzero(apr.data)
may1 = np.count_nonzero(may.data)
june1 = np.count_nonzero(june.data)
plot_set = np.array([jan1,feb1,mar1,apr1,may1,june1])
plot_set


#make an empty plot
fig1 = plt.figure(figsize=(50,50))
width = 0.35

#plotting
ax0 = fig1.add_subplot(1,1,1)
ax0.bar(x, plot_set, width, label='Men')
ax0.plot(plot_set,color = 'pink', linestyle = '--',linewidth = 10)

#set labels
x_label = ['January', 'Febury', 'March', 'April', 'May', 'June']
ax0.set_title('Impact of COVID-19 on airlines')
x = np.arange(len(x_label))
ax0.set_xticks(x)
ax0.set_xticklabels(x_label)

#plot adjustments
matplotlib.rc('xtick', labelsize=50)     
matplotlib.rc('ytick', labelsize=50)
plt.rcParams.update({'font.size': 60})
plt.xlabel('Month \n \n This plot shows how Covid-19 has impacted global commercial flight market in the first half of 2020', fontsize=50)
plt.ylabel('Total number of observed flights per month(in milion)', fontsize=50)
matplotlib.pyplot.grid(color='black', linestyle='-', linewidth=2)


#show the plot
plt.show()
