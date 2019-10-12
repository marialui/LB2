# !/usr/bin/python
import os, sys
import sys
import numpy as np
import pandas as pd

def information(beta,coil,helix,aa,ss):
    Ph=float(ss.loc['H'])
    PrPh= aa.multiply(float(Ph))
    Ih=(np.log10((helix.div(PrPh.values).astype(float))))
    Pe=float(ss.loc['E'])
    PrPe = aa.multiply(float(Pe))
    Ie =np.log10(( beta.div(PrPe.values).astype(float)))
    Pc =float( ss.loc['C'])
    PrPc = aa.multiply(float(Pc))
    Ic=np.log10(coil.div((PrPc.values).astype(float)))
    #print(Ie)
    ll=[Ie,Ih,Ic]
    return(ll)


def prediction(IFs):
    for item in os.listdir("/home/um77/project/fasta_blindset/profile"):
        if '%s' % (item.split('.')[1]) == 'profile':
            stuff = '%s' % (item.split('.')[0]) + '.DSSP'
            pro = pd.read_fwf('/home/um77/project/fasta_blindset/profile/%s' % ( item), sep="\t")
            pro.drop(pro.columns[0], axis=1, inplace=True)
            #print(item, stuff)

            dssp = open('/home/um77/project/dssp_blindset/predictedDSSP/%s' % (stuff), 'w')
            DSSP=''

            residues = (pro.shape[0] + 16)

            new = np.zeros(shape=((residues, 20)))
            profili = pd.DataFrame(new,
                                   columns=['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P',
                                            'S', 'T', 'W',
                                            'Y', 'V'])
            pro.index = pro.index + 8
            # here df is the dataframe containing the profile plus 10 row at the end and at the beginning with all zeros.
            df = pro.combine_first(profili)
            #print(df)
            structure = ['E', 'H', 'C']
            d={0:'E',1:'H',2:'C'}


            for i in range(8, df.shape[0] - 8):
                valori = []


                for m in range(len(structure)):
                    profile = df.iloc[i - 8:i + 9]
                    globals()[structure[m]]=(IFs[m].astype(float)).multiply((profile.values))
                    value= (globals()[structure[m]]).values.sum()
                    valori.append(value)
                massimo=max(valori)
                DSSP=DSSP +'%s'%d[valori.index(massimo)]
            dssp.write('>%s'%(item.split('.')[0]) +'\n%s'%(DSSP))











if __name__ == "__main__":

    n = np.arange(17)
    index0 =pd.MultiIndex.from_product([list(n), ['E']])
    strand = pd.read_csv('%s' % sys.argv[1], delimiter=',').set_index(index0)

    index1 = pd.MultiIndex.from_product([list(n), ['C']])
    coil = pd.read_csv('%s' % sys.argv[2], delimiter=',').set_index(index1)
    index2 = pd.MultiIndex.from_product([list(n), ['H']])
    helix = pd.read_csv('%s' % sys.argv[3], delimiter=',').set_index(index2)
    index3 = pd.MultiIndex.from_product([list(n), ['R']])
    residue = pd.read_csv('%s' % sys.argv[4], delimiter=',').set_index(index3)

    structures=pd.read_csv('%s' % sys.argv[5], delimiter=',')
    strutture=['H', 'E', 'C']
    structures.index = strutture

    risultati= information(strand,coil,helix,residue,structures)
    dizionario = {0: 'strand', 1: 'helics', 2: 'coil'}

    for rs in range(len(risultati)):
        export_csv = risultati[rs].to_csv('%sIF.csv' % (dizionario[rs]), index=None, header=True)


    prediction(risultati)