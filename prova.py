import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
ss=['HE---EH']
fasta=['AKTCAAA']
composition={}
residuepercentage={}
for m in range(len(ss)):

    # print (m)
    # print (ss[m], fasta[m])
    # print(len(ss[m]),len(fasta[m]))

    for n in range(len(ss[m])):
        # print(ss[m][n])
        if ss[m][n] in composition:

            if fasta[m][n] in composition[ss[m][n]] :
                #print('*****' ,composition[ss[m][n]])
                composition[ss[m][n]][fasta[m][n]] = composition[ss[m][n]][fasta[m][n]] + 1
                #print(+5)
                # print(fasta[m][n])
                # composition[ss[m][n]] = dizionario
                #print(composition)
            else:
                composition[ss[m][n]][fasta[m][n]] = 1
                # print(fasta[m][n])

            #composition[ss[m][n]] = dizionario

            # print(dizionario)

        else:
            dizionario = {}
            dizionario[fasta[m][n]] = 1
            #print('<<<',dizionario)
            composition[ss[m][n]] = dizionario
            # print(composition)

    # print(composition[ss[m][n]])
print(composition)
# print(m,n)
for m in range(len(fasta)):

    for n in range(len(fasta[m])):
        # print(ss[m][n])
        if fasta[m][n] in residuepercentage:

            if ss[m][n] in residuepercentage[fasta[m][n]]:
                residuepercentage[fasta[m][n]][ss[m][n]] = residuepercentage[fasta[m][n]][ss[m][n]] + 1

            else:
                residuepercentage[fasta[m][n]][ss[m][n]] = 1

        else:
            dizionario = {}
            dizionario[ss[m][n]] = 1
            residuepercentage[fasta[m][n]] = dizionario
print('here is the relative composition:',residuepercentage)  # this prints a dictionary where for each ss we have associated the corrispective number of residue
# prensent in that ss.

d = residuepercentage
secodary_structure = d['score_india']
legend = ['overall', 'helix','strand','coil']
score_pk = d['score_pk']
plt.hist([score_india, score_pk], color=['orange', 'green'])
plt.xlabel("Residues")
plt.ylabel("Residues Frequency")
plt.legend(legend)
plt.xticks(range(0, 7))
plt.yticks(range(1, 20))
plt.title('Champions Trophy 2017 Final\n Runs scored in 3 overs')
plt.show()


