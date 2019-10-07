#!/usr/bin/python
import sys
import numpy as np
import pandas as pd
d={'E':'E','H':'H','-':'C'}
#with this function it automatically produces 4 matrices:
#one for helixes(H), one for strand(E), one for coil (C) and one for the frequency of each residue (R)

def gor_training(pro,dssp):
    global profile
    n=np.arange(18)

    ss=[['H'],['E'],['C'],['R']]
    for structure in (ss):
        index=pd.MultiIndex.from_product([n, structure])
        matrix = pd.DataFrame(index=index,
                     columns=['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W',
                              'Y', 'V'])
        for col in matrix.columns:
            matrix[col].values[:] = 0
        globals()[structure[0]]=matrix
    #ora che abbiamo generato le matrici dobbiamo riempirle:
    lines=dssp.readlines()

    residues=(pro.shape[0] + 16)
    new = np.zeros(shape=((residues, 20)))
    profili= pd.DataFrame(new , columns=['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W',
                              'Y', 'V'])
    pro.index= pro.index+8
#here df is the dataframe containing the profile plus 10 row at the end and at the beginning with all zeros.
    df = pro.combine_first(profili)



    structure=['0' for m in range(8)]
    for s in (lines[1].strip()):
        structure.append(d[s])
    for k in range(8):
        structure.append('0')


    for i in range (8, df.shape[0]-9):
        v=i+1
        for m in range(i, i-9, -1):
            c = 8-(i - m)
            profile = df.iloc[m]
            globals()[structure[i]].loc[c].update(globals()[structure[i]].loc[c] + profile)
            f = 8 + (v - i)
            profile1=df.iloc[v]
            globals()[structure[i]].loc[f].update(globals()[structure[i]].loc[f] + profile1)
            v = v + 1
            globals()['R'].loc[c].update(globals()['R'].loc[c] + profile)
            globals()['R'].loc[f].update(globals()['R'].loc[f] + profile1)

    for mat in ss:
        print(globals()[mat[0]].div(len(structure)-16).round(2))



if __name__ == "__main__":
    profile= pd.read_fwf('%s' %sys.argv[1], sep="\t")
    profile.drop(profile.columns[0],axis=1,inplace=True)
    dsspfile=open('%s' %sys.argv[2], 'r')
    gor_training(profile, dsspfile)