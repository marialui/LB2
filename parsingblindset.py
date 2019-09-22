import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd
data = pd.read_csv('blindset.csv', sep=",", header=0)
data1=((data.drop('Chain ID',axis=1)).drop('Resolution',axis=1)).drop('Sequence',axis=1)
# dropping duplicate values : same id, same chain length
data1.drop_duplicates(keep='first',inplace=True)
intersected_df = data[data.index.isin(data1.index)]
#print(intersected_df.head())
res = intersected_df.set_index('PDB ID')['Resolution']

#create a fasta file from the list of pdb chains we retained.
f4=open('PDB.fasta','w')
for j in range(len(intersected_df['PDB ID'])):
    f4.write('>' + (intersected_df['PDB ID'].iloc[j]).lower()+'_'+ intersected_df['Chain ID'].iloc[j] + '\n' + \
             intersected_df['Sequence'].iloc[j] + '\n'
             )
#import cluster file as dataframe

clust=pd.read_csv('clust.txt', sep="\n", header=0)
clust.columns = ['clusters']

#print(clust)


#create a dictionary from the dataframe where we have the id :resolution
#print (intersected_df)
Res=(intersected_df).drop('Sequence',axis=1).drop('Chain Length',axis=1)
forfasta=(intersected_df).drop('Chain Length',axis=1)
forfasta['Name'] = (forfasta['PDB ID']).str.cat(forfasta['Chain ID'],sep="_")
Res['Name'] = (Res['PDB ID']).str.cat(Res['Chain ID'],sep="_")
Res1=(Res.drop('Chain ID',axis=1)).drop('PDB ID',axis=1)
forfasta1=((forfasta.drop('Chain ID',axis=1)).drop('PDB ID',axis=1)).drop('Resolution', axis=1)
Res1=Res1[['Name','Resolution']]
forfasta1=forfasta1[['Name','Sequence']]
#print(forfasta1)
df_dict = dict(zip(Res1.Name, Res1.Resolution))
#print (df_dict)
lun=(clust.shape)[0]
best=[]

#now create a list best in which will be stored the best id for each cluster, the one with
#the best resolution.
for m in range (0,lun):

    cluster = (clust['clusters'].iloc[m]).split()
    if sum(cluster.index(x) for x in cluster) > 1:
        best_id = []
        for pid in cluster:
            v = df_dict.get(pid, float('inf'))
            best_id.append([v, pid])
        best_id.sort()
        best.append(best_id[0][1])
    else:
        best.append(cluster[0])
#print(best_id)

#so best is the list made of the best representative for each clustering on the basis of the best resolution.
print('hi i am the length' , len(best))
#best_fasta = best[best.index.isin(intersected_df.index)]
#print(best)

#and we will put this list into a file 'representatives.txt in wich we will have all the ids of representative
#structures , one for each cluster on the basis on the best resolution.
f5=open('representatives.txt','w')
for k in range(len(best)):
    f5.write(best[k] + '\n')

#HERE WE FIRST BUILD THE DATAFRAME COMPOSED BY THE COLUMN NAME WITH ALL THE IDS OF THE REPRESENTATIVES
#THEN WE MERGED THIS DATAFRAME WITH THE FORFASTA1 INITIAL ONE WHERE WE SOTRED FOR ALL THE IDS WE STARTED FROM
#THE CORRISPONDENT SEQUENCE
representatives = pd.DataFrame(best)
representatives.columns = ['Name']
print(representatives)
print(forfasta1)
Fasta = pd.merge(representatives, forfasta1, how='inner', on=['Name'])
print(Fasta)

#here we store in file representatives.fasta all the ids of all the representatives
#and the corrispondent sequence in fasta format
f6=open('representatives.fasta','w')
for L in range(len(Fasta['Name'])):
    f6.write('>' + (Fasta['Name'].iloc[L]).lower()+ '\n'+ Fasta['Sequence'].iloc[L] + '\n' )