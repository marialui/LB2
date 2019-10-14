# !/usr/bin/python
import os, sys
import sys
import numpy as np
import pandas as pd

d = {'E': '2', 'H': '1', '-': '3'}


# with this function it automatically produces 4 matrices:
# one for helixes(H), one for strand(E), one for coil (C) and one for the frequency of each residue (R)

# here pro and dssp should be the path
def svm_training(pathprofile, pathdssp):
    outputfile = open("ss.train.dat", "w+")

    # ora che abbiamo generato le matrici dobbiamo riempirle:

    for item in os.listdir(pathprofile):
        if '%s' % (item.split('.')[1]) == 'profile':
            stuff = '%s' % (item.split('.')[0]) + '.dssp'
            pro = pd.read_fwf('%s/%s' % (pathprofile, item), sep="\t")
            pro.drop(pro.columns[0], axis=1, inplace=True)
            print(item, stuff)

            dssp = open('%s/%s' % (pathdssp, stuff), 'r')
            # global profile
            lines = dssp.readlines()
            residues = (pro.shape[0] + 16)

            new = np.zeros(shape=((residues, 20)))
            profili = pd.DataFrame(new,
                                   columns=['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P',
                                            'S', 'T', 'W',
                                            'Y', 'V'])
            pro.index = pro.index + 8
            # here df is the dataframe containing the profile plus 10 row at the end and at the beginning with all zeros.
            df = pro.combine_first(profili)

            structure = ['0' for m in range(8)]
            for s in (lines[1].strip()):
                structure.append(d[s])
            for k in range(8):
                structure.append('0')

            # from now on i'm filling the matrices
            #
            l = []

            for i in range(8, df.shape[0] - 8):

                row = [structure[i]]


                profile = df.iloc[i - 8:i + 9].to_numpy()
                print('profile is >>>', profile)
                for e in range (len(profile)):
                    for element in profile[e]:
                        l.append(element)
                for j in l:
                    if j != 0:
                        row.append('%d:%f'%(int(l.index(j))+1,float(j)))
                print(row)
                s = " ".join(row)

                outputfile.write('%s\n'%(s))
                l = []
                row = []



                    #row.append('%s:%s'%(l.index(element),element))
                    #print('row is :>>>>', row)
                l=[]
                #row=[]
               # print(row)

                #profile is the windw of 17 rows and 20 columns





if __name__ == "__main__":
    pathprofile = sys.argv[1]
    pathdssp = sys.argv[2]


    matrici = svm_training(pathprofile, pathdssp)
    print(matrici)












