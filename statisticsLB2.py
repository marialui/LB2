#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import functions as f
import pandas as pd

if __name__ == "__main__":
    ss = open(sys.argv[1], "r")
    fasta = open(sys.argv[2], "r")
    data = open(sys.argv[3], "w+")

    set = f.merger(ss, fasta)

    m= (f.ss_percentage(data))
    l=m[0]
    #print(l)
    #f.printpie(l)
    stru=m[1]
    fas=m[2]
    residui = (f.aa_percentage(fas,stru))
    print(residui)
    f.print_histogram(residui)
