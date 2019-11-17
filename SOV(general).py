# !/usr/bin/python
import os, sys
import sys
import re
import numpy as np

lista = ['H', 'C', 'E']


def SOV(observed, predicted):
    for i in lista:
        globals()['num_%s' % (i)] = 0
        globals()['totalsov_%s' % (i)] = 0

    for item in os.listdir(observed):

        if '%s' % (item.split('.')[1]) == 'dssp':
            stuff = '%s' % (item.split('.')[0]) + '.DSSP'
            pred = open('%s/%s' % (predicted, stuff), 'r')
            obs = open('%s/%s' % (observed, item), 'r')

            P = pred.readlines()[1]
            O = obs.readlines()[1]

            # O='CCCHHHHHCCCCCCCCHHHHHHHHHHCCC'
            # P='CCCCCCCCCCCHHHHHHHCCCCCHHHHCC'
            for i in lista:
                globals()['LISTAP_%s' % (i)] = []
                globals()['LISTAO_%s' % (i)] = []
                globals()['sommatoria_%s' % (i)] = []
                globals()['N%s' % (i)] = O.count(i)
                if globals()['N%s' % (i)]!=0:
                    globals()['SOV%s' % (i)] = 100 * (1 / globals()['N%s' % (i)])
                else:
                    globals()['SOV%s' % (i)]=0
                globals()['C%s' % (i)] = re.compile("%s*" % (i))
                for L in globals()['C%s' % (i)].finditer(P):
                    if i in (L.group()):
                        globals()['LISTAP_%s' % (i)].append(L.span())
                for J in globals()['C%s' % (i)].finditer(O):
                    if i in (J.group()):
                        globals()['LISTAO_%s' % (i)].append(J.span())
                for el in globals()['LISTAP_%s' % (i)]:
                    for el1 in globals()['LISTAO_%s' % (i)]:
                        globals()['sp_%s' % (i)] = set(np.arange(*el))  # predicted
                        globals()['so_%s' % (i)] = set(np.arange(*el1))  # observed
                        globals()['intersec_%s' % (i)] = globals()['sp_%s' % (i)].intersection(globals()['so_%s' % (i)])
                        if globals()['intersec_%s' % (i)] != set():
                            globals()['MINOV_%s' % (i)] = len(globals()['intersec_%s' % (i)])
                            globals()['MAXOV_%s' % (i)] = len(globals()['sp_%s' % (i)]) + len(
                                globals()['so_%s' % (i)]) - globals()['MINOV_%s' % (i)]
                            globals()['correction_%s' % (i)] = [
                                (globals()['MAXOV_%s' % (i)] - globals()['MINOV_%s' % (i)]),
                                globals()['MINOV_%s' % (i)], \
                                (len(globals()['sp_%s' % (i)]) / 2), (len(globals()['so_%s' % (i)]) / 2)]
                            globals()['sig_%s' % (i)] = min(globals()['correction_%s' % (i)])
                            globals()['value_%s' % (i)] = ((globals()['MINOV_%s' % (i)] + globals()['sig_%s' % (i)]) /
                                                           globals()['MAXOV_%s' % (i)]) * len(globals()['so_%s' % (i)])
                            globals()['sommatoria_%s' % (i)].append(globals()['value_%s' % (i)])

                globals()['sov%s' % (i)] = globals()['SOV%s' % (i)] * (sum(globals()['sommatoria_%s' % (i)]))

                if globals()['sov%s' % (i)] != 0:
                    globals()['num_%s' % (i)] = globals()['num_%s' % (i)] + 1
                if globals()['num_%s' % (i)]!=0:
                    globals()['totalsov_%s' % (i)] = globals()['totalsov_%s' % (i)] + globals()['sov%s' % (i)]
                    globals()['average%s' % (i)] = globals()['totalsov_%s' % (i)] / globals()['num_%s' % (i)]
                else:
                    globals()['average%s' % (i)]=0


    return (averageH, averageE,averageC)


if __name__ == "__main__":
    pathobserveddssp = sys.argv[1]
    pathpredicteddssp = sys.argv[2]
    result = SOV(pathobserveddssp, pathpredicteddssp)
    print('respective SOVs for H, E and C are: ', result)
