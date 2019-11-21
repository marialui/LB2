#!/usr/bin/python
import cufflinks as cf
import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd
data = pd.read_csv('Scop.csv', sep=",", header=None)
data.columns = ["letter", "domain",]
df = data.drop_duplicates(subset=['letter'])
#print (df)
data1 = pd.read_csv('scopid.csv', sep=",", header=None,)
statistica=pd.DataFrame(data1.apply(pd.value_counts).reset_index().values,columns=['letter', 'count'])
dfB=(statistica.sort_values('letter'))
#print(statistica.shape)
s1 = pd.merge(df, dfB, how='inner', on=['letter'])

cmap = plt.get_cmap('Spectral')
colors = [cmap(i) for i in np.linspace(0, 1, 12)]
s1 = s1.sort_values(['count'], ascending = False)
print(s1)
s1.drop(s1.tail(7).index,inplace=True)
print(s1)
df2 = pd.DataFrame({'letter':['m'],"domain":['others'],
                    "count":[21685]})
s1=s1.append(df2,ignore_index = True)
print(df2,'\n',s1)

#colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]

# Create a pie chart
plt.pie(
    # using data total)arrests
    s1['count'],
    # with the labels being officer names
    #labels=s1['letter'],
    # with no shadows
    shadow=False,
    # with colors
    colors=colors,
    # with one slide exploded out
    #explode=(0, 0, 0, 0, 0.15),
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction

    autopct='%.2f')

# View the plot drop above
plt.axis('equal')
plt.title('scop classification')
plt.legend(s1['domain'],loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
# View the plot
plt.tight_layout()
plt.show()
