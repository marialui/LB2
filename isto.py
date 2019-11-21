import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd

residuepercentage= {'K': {'-': 5.79, 'E': 5.04, 'H': 6.87}, 'V': {'-': 4.38, 'E': 13.42, 'H': 6.56}, 'S': {'-': 7.25, 'E': 5.02, 'H': 4.45}, 'H': {'-': 2.47, 'E': 2.26, 'H': 1.95}, 'R': {'-': 4.57, 'E': 4.93, 'H': 6.19}, 'T': {'-': 5.86, 'E': 6.6, 'H': 4.19}, 'E': {'-': 6.28, 'E': 4.78, 'H': 9.59}, 'P': {'-': 7.85, 'E': 2.23, 'H': 1.93}, 'G': {'E': 4.94, '-': 11.82, 'H': 3.24}, 'L': {'E': 9.95, '-': 6.62, 'H': 12.26}, 'Q': {'E': 2.88, '-': 3.36, 'H': 4.93}, 'D': {'-': 8.13, 'E': 3.28, 'H': 4.61}, 'N': {'-': 5.64, 'E': 2.58, 'H': 2.97}, 'M': {'-': 1.73, 'E': 2.09, 'H': 2.66}, 'A': {'E': 6.41, '-': 6.65, 'H': 11.72}, 'I': {'-': 3.24, 'E': 9.56, 'H': 6.21}, 'C': {'E': 1.7, '-': 1.39, 'H': 1.05}, 'Y': {'E': 4.95, '-': 2.68, 'H': 3.22}, 'F': {'E': 5.48, '-': 3.11, 'H': 3.94}, 'W': {'E': 1.81, 'H': 1.39, '-': 1.09}, 'X': {'-': 0.0}}


print(residuepercentage)

def print_histogram(data):
    combined_df =pd.DataFrame(residuepercentage)
    print(combined_df)
    df_transposed = combined_df.T
    df_transposed.plot.bar()

    plt.show()
print_histogram(residuepercentage)