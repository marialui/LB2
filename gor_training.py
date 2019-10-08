#!/usr/bin/python
import sys
import numpy as np
import pandas as pd
d={'E':'E','H':'H','-':'C'}
#with this function it automatically produces 4 matrices:
#one for helixes(H), one for strand(E), one for coil (C) and one for the frequency of each residue (R)

#here pro and dssp should be the path
def gor_training(pro,dssp):
    global profile
    n=np.arange(17)

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

    #creare un contatore di strutture secondarie
    HEC = pd.DataFrame([0,0,0], index=['H', 'E', 'C'],columns=['Number of SS'])


#from now on i'm filling the matrices
    for i in range (8, df.shape[0]-8):
        midx = pd.MultiIndex.from_product([list(n),[structure[i]]])
        midx1 = pd.MultiIndex.from_product([list(n), ['R']])
        profile = df.iloc[i-8:i+9]
        profile1 = profile.set_index(midx1)
        profile=profile.set_index(midx)
        (globals()[structure[i]]).update(globals()[structure[i]]+ profile)

            #UPDATE RESIDUE MATRIX
        globals()['R'].update(globals()['R'] + profile1)

            #UPDATE SECONDARY STRUCTURE MATRIX
        HEC.loc[structure[i]] = HEC.loc[structure[i]] + 1


    for mat in ss:
        globals()[mat[0]]= globals()[mat[0]].div(len(structure) - 16).round(2)
    return (E,H,C,R,(HEC.div(len(structure) - 16).round(2)))



if __name__ == "__main__":
    profile= pd.read_fwf('%s' %sys.argv[1], sep="\t")
    profile.drop(profile.columns[0],axis=1,inplace=True)
    dsspfile=open('%s' %sys.argv[2], 'r')
    results=gor_training(profile, dsspfile)
    for maj in results:
        print(maj,'\n')