#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd

lista = ['percentage of coil', 'percentage of strends', 'percentage of helixes']
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





def ss_percentage(set):
    c = 0
    e = 0
    h = 0
    t = 0
    file=[]
    ss=[]
    fasta=[]
    id=[]
    counts = {}
    residuepercentage={}

    for line in set:
        line=line.rstrip()
        if line[0]!='>':
            file.append(line)
        else:id.append(line[1:])
    for j in range (0,len(file),2):
        ss.append(file[j])
        if j!= 0:
            fasta.append(file[j-1])



        for i in file[j]:
            if i == 'E':
                e = e + 1
                t = t + 1
            elif i == 'H':
                h = h + 1
                t = t + 1
            elif i == '-':
                c = c + 1
                t = t + 1
    #print(id)
    #fasta.append(file[len(file) - 1])
    coil = (float(c / t) * 100)
    helix = (float(h / t) * 100)
    strand = (float(e / t) * 100)
    #for k in range(-1, len(file) , 2):
        #fasta.append(file[k])
    for i in range(len(fasta)):
        for aa in fasta[i]:
            #print(aa)
            if aa in counts:
                counts[aa] = counts[aa] + 1
            else :
                counts[aa] = 1
    strutturesecondarie={}
    for i in range(len(ss)):
        for sec in ss[i]:
            # print(aa)
            if sec in strutturesecondarie:
                strutturesecondarie[sec]=strutturesecondarie[sec] +1
            else:
                strutturesecondarie[sec] = 1
    print(strutturesecondarie)
   # print ('here is the total count:' ,counts) #this prints a vocabulary where each residue is associated to the number of times it appears

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
            residuepercentage[aa][s]= round(float (residuepercentage[aa][s]/strutturesecondarie[s])*100,2)
            #print(residuepercentage[aa][s],strutturesecondarie[s])

    print('here is the relative composition:',residuepercentage)  # this prints a dictionary where for each ss we have associated the corrispective number of residue
    # prensent in that ss.
    return ([coil, strand, helix],residuepercentage)




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


def print_histogram(data):
    combined_df =pd.DataFrame(data)
    print(combined_df)
    df_transposed = combined_df.T
    df_transposed.plot.bar()

    plt.show()


#we took the pdb ids and with the advance search in pdb we retrieved
#the number of ids for each kindom and we plot the result
def kindom_pie(listk):
    tot = sum(listk)
    for i in range(len(listk)):
        listk[i]=round(float((listk[i]/tot))*100,1)
    #print(listk,kindo)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Bacteria','Eukaryota','Archaea','Viruses','Other'
    sizes = listk
    explode = (0, 0, 0, 0.4,0.7)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


if __name__ == "__main__":
    ss = open(sys.argv[1], "r")
    fasta = open(sys.argv[2], "r")
    data = open(sys.argv[3], "w+")

    set = merger(ss, fasta)
    m=ss_percentage(data)
    l = (m[0])
    print(l)
    printpie(l)
    residui=(m[1])
    print(residui)
    print_histogram(residui)
    listak = [639, 455, 93, 63, 2]
    kindom_pie(listak)
