## This module to handle reading and writing with csv files
""" Author Name: Anbara Al-Jamal
    Author ID: 150107
    This code is available as an open-source file
"""
import pandas as pd
import zipfile as zf
import scipy.io as sp
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import os


def read_csv_file(file_path):
    return pd.read_csv(file_path)

def read_excel_file(file_path):
    return pd.read_excel(file_path)

def first_n_dps(data_frame, number_of_lines):
    data = data_frame.iloc[:number_of_lines]
    return data
    
def last_n_dps(data_frame, number_of_lines):
    data = data_frame.iloc[-number_of_lines:]
    return data

def read_from_zip(path, file_name):
    zipped = zf.ZipFile(path)
    data = pd.read_excel(zipped.open(file_name))
    return data

def read_mat(file_name):
    data = sp.loadmat(file_name)
    return data

def display_mat_plot(data, outDir, outFile):
    X = data['x']
    Y = data['y']
    U = data['z']
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, U, rstride=1, cstride=1, cmap=cm.jet)
    fig.colorbar(surf)
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    plt.show()



