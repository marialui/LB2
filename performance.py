# !/usr/bin/python
import os, sys
import sys
import numpy as np
import pandas as pd
import math
d = {'E': 'E', 'H': 'H', '-': 'C', 'C':'C'}
lista=['H','C','E']

def performance(observed, predicted):
    total=0
    HEC = pd.DataFrame([[0, 0, 0], [0, 0, 0], [0, 0, 0]], index=['H', 'E', 'C'], columns=['H', 'E', 'C'])

    for item in os.listdir(observed):
        if '%s' % (item.split('.')[1]) == 'dssp':
            stuff = '%s' % (item.split('.')[0]) + '.DSSP'
            pred = open('%s/%s' % (predicted, stuff), 'r')
            obs = open('%s/%s' % (observed,item), 'r')
            P = pred.readlines()[1]
            O=obs.readlines()[1]
            total=total+len(P)
            for i in range(len(P)):
                HEC.loc[d[P[i]]].loc[d[O[i]]]=HEC.loc[d[P[i]]].loc[d[O[i]]]+1

    return(HEC, total)

def binary_scoring(tab):

    perf=[]
    for i in lista:
        globals()['C%s'%(i)]=tab.loc[i].loc[i]
        globals()['O%s'%(i)]= (tab.loc[i].sum())-globals()['C%s'%(i)]
        globals()['U%s'%(i)]=(tab.loc[:,i].sum())-globals()['C%s'%(i)]
        globals()['N%s'%(i)]=(((tab.drop(index='%s'%(i), columns='%s'%(i)))).values).sum()
        globals()['SEN%s' % (i)]=globals()['C%s'%(i)]/(globals()['C%s'%(i)]+globals()['U%s'%(i)])
        globals()['PPV%s' % (i)]=globals()['C%s'%(i)]/(globals()['C%s'%(i)]+globals()['O%s'%(i)])
        num=(globals()['C%s'%(i)]*globals()['N%s'%(i)])-(globals()['O%s'%(i)]*globals()['U%s'%(i)])
        den=math.sqrt((globals()['C%s'%(i)]+ globals()['O%s'%(i)])*(globals()['C%s'%(i)]+ globals()['U%s'%(i)])\
                *(globals()['N%s'%(i)]+globals()['O%s'%(i)])*(globals()['N%s'%(i)]+globals()['U%s'%(i)]))
        globals()['MCC%s' % (i)]=num/den


        globals()['performance_%s' % (i)]=['PERFORMANCE %s :' %(i),'SEN_%s= '%(i),globals()['SEN%s' % (i)], 'PPV_%s= '% (i),globals()['PPV%s' % (i)],'MMC_%s= '%(i),globals()['MCC%s' % (i)]]
        perf.append(globals()['performance_%s' % (i)])

    return (perf)




if __name__ == "__main__":
    pathobserveddssp = sys.argv[1]
    pathpredicteddssp = sys.argv[2]
    result=performance(pathobserveddssp,pathpredicteddssp)
    confusion_matrix = result[0]
    totale=result[1]
    matrice=confusion_matrix.to_numpy()
    #print(totale)
    Q=((matrice.diagonal()).sum())/totale #this is the accuracy

    print(confusion_matrix)
    for i in (binary_scoring(confusion_matrix)):
        print(i,'\n')
    print('Three-class accuracy Q3 = %s' % (Q))