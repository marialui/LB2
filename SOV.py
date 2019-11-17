# !/usr/bin/python
import os, sys
import sys
import re
import numpy as np

d = {'E': 'E', 'H': 'H', '-': 'C', 'C':'C'}
def SOV(observed, predicted):
    for item in os.listdir(observed):
        if '%s' % (item.split('.')[1]) == 'dssp':
            stuff = '%s' % (item.split('.')[0]) + '.DSSP'
            pred = open('%s/%s' % (predicted, stuff), 'r')
            obs = open('%s/%s' % (observed,item), 'r')
            #P = pred.readlines()[1]
            #O=obs.readlines()[1]
            O='CCCHHHHHCCCCCCCCHHHHHHHHHHCCC'
            P='CCCCCCCCCCCHHHHHHHCCCCCHHHHCC'

            LISTAP=[]
            LISTAO=[]
            sommatoria=[]
            Nh=O.count('H')
            SOVh=(100*(1/Nh))
            C=re.compile("H*")
            for L in C.finditer(P):
                if 'H' in ( L.group()):
                    LISTAP.append(L.span())
            for J in C.finditer(O):
                if 'H' in (J.group()):
                    LISTAO.append(J.span())
            for el in LISTAP:
                for el1 in LISTAO:
                    sp = set(np.arange(*el)) #predicted
                    so= set(np.arange(*el1))  #observed
                    intersec= sp.intersection(so)
                    if intersec != set():

                        MINOV=len(intersec)
                        MAXOV=len(sp)+len(so)-MINOV
                        correction=[(MAXOV-MINOV),MINOV,(len(sp)/2),(len(so)/2)]
                        sig=min(correction)
                        value=((MINOV+sig)/MAXOV)*len(so)
                        sommatoria.append(value)

            sov= SOVh*(sum(sommatoria))
            return(sov)

if __name__ == "__main__":
    pathobserveddssp = sys.argv[1]
    pathpredicteddssp = sys.argv[2]
    result=SOV(pathobserveddssp,pathpredicteddssp)
    print('sov is ',result)
