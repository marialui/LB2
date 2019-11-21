#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd
# this will take as an input 2 files: the first one with all the ss , the second is a fasta file
# and will return a merged file where for each id the secondary structure and the fasta is reported

def merger(f1, f2):
    l1 = f1.readlines()
    l2 = f2.readlines()
    f3 = open("maintext", "w+")
    for i in l1:

        if i[0] == ">":
            f3.write(i)
            f3.write(l1[l1.index(i) + 1])
            for j in l2:
                if j in i:
                    f3.write(l2[l1.index(j) + 1])
                else:
                    continue
        else:
            continue
    return (f3)


#this function will count the number of residues that are present in each secondary structure and will return the
#relative percentages

def ss_percentage(set):
    c = 0
    e = 0
    h = 0
    k = 0
    file=[]
    ss=[]
    fasta=[]

    for line in set:
        line=line.rstrip()
        if line[0]!='>':
            file.append(line)
    for j in range (0,len(file),2):
        ss.append(file[j])
        if j!= 0:
            fasta.append(file[j-1])
        #print (file[j])


        for i in file[j]:

            if i == 'E':
                e = e + 1
                k = k + 1

            elif i == 'H':
                h = h + 1
                k = k + 1

            elif i == '-':
                c = c + 1
                k = k + 1


    #print(ss,fasta)

    fasta.append(file[len(file) - 1])
    print(k)
    coil = float(c / k)* 100
    print(coil)
    helix = float(h / k) * 100
    strand = float(e / k) * 100

    return ([coil, strand, helix],fasta,ss)

def aa_percentage(fasta,ss):

    residuepercentage = {}
    strutturesecondarie = {}
    for i in range(len(ss)):
        for sec in ss[i]:
                # print(aa)
            if sec in strutturesecondarie:
                strutturesecondarie[sec] = strutturesecondarie[sec] + 1
            else:
                strutturesecondarie[sec] = 1
        #print(strutturesecondarie)
        # print ('here is the total count:' ,counts) #this prints a vocabulary
        # where each ss is associated to the number of times it appears

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

    for aa in residuepercentage:
        for s in residuepercentage[aa]:
            residuepercentage[aa][s] = round(float(residuepercentage[aa][s] / strutturesecondarie[s]) * 100, 2)
                 #print(residuepercentage[aa][s],strutturesecondarie[s])



    print('here is the relative composition:',
              residuepercentage)  # this prints a dictionary where for each residue we have associated another dictionary
        #where for each secondary structure we have the relative percentage of that specific residue in that specific secondary
        #structure over the total number of residues in that secondary structure
    return(residuepercentage)
#this is a function that takes the percentage of coil , elixes and strand and plot it in a pie chart
def printpie(a):
    b = ['percentage of coil', 'percentage of strends', 'percentage of helixes']
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    wedges, texts = ax.pie(a, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(b[i] + ' is ' + '{0:.2f}%'.format(round(a[i]), 2), xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                    horizontalalignment=horizontalalignment, **kw)

    ax.set_title("SS composition")

    plt.show()

#this is a function that takes the residues persentage and the relative composition in
#secondary structure and gives backs the histogram
def print_histogram(data):
    combined_df =pd.DataFrame(data)
    #print(combined_df)
    df_transposed = combined_df.T
    df_transposed.plot.bar()

    plt.show()