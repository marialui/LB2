#!/usr/bin/python
import sys
import numpy as np
import pandas as pd
import json

def parsingpssm(data,out):
    profile=data[data.columns[19:-2]]
    profile= profile.set_axis(['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'], axis=1, inplace=False)
    profile=profile.droplevel([0,1,3])
    profile=(profile.div(100).round(2))
    example_string = profile.to_string()
    output_file = open('%s' %out,'w')
    output_file.write(example_string)
    output_file.close()

if __name__ == "__main__":
    file= pd.read_csv('%s' %sys.argv[1], sep='\t', index_col=None)
    output= sys.argv[2]
    parsingpssm(file, output)