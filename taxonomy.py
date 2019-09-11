#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd
data = pd.read_csv("taxonomy.csv")
# Preview the first 5 lines of the loaded data
#print(data.head())
taxa=data.iloc[::,2:]
total=taxa.describe()
#print(total)
#crime_year = pd.DataFrame(df_1.year.value_counts(), columns=["Year", "AggregateCrime"])
Others=2750-1203
main=pd.DataFrame(taxa.apply(pd.value_counts)[:10].reset_index().values,columns=['source', 'n'])
main=main.append({'source' : 'Others' , 'n' : Others} , ignore_index=True)
#total 2750
#maincount=int(main.sum()) #1203 belongs to main taxa
# Create a list of colors (from iWantHue)
colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]

# Create a pie chart
plt.pie(
    # using data total)arrests
    main['n'],
    # with the labels being officer names
    labels=main['source'],
    # with no shadows
    shadow=False,
    # with colors
    colors=colors,
    # with one slide exploded out
    #explode=(0, 0, 0, 0, 0.15),
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%1.1f%%',
    )

# View the plot drop above
plt.axis('equal')

# View the plot
plt.tight_layout()
plt.show()
