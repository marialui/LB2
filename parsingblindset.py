import cufflinks as cf
import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd
data = pd.read_csv('blindset.csv', sep=",", header=0)
data1=(data.drop('Chain ID',axis=1)).drop('Resolution',axis=1)
# dropping duplicate values
data1.drop_duplicates(keep='first',inplace=True)
intersected_df = data[data.index.isin(data1.index)]
print(intersected_df.head())
print(intersected_df.shape)
f3 = open("pdbids", "w+")
for i in range(len(intersected_df['PDB ID'])):
    f3.write((intersected_df['PDB ID'].iloc[i]+'_').lower() + intersected_df['Chain ID'].iloc[i]+'\n')
