import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def input_file(filename):
    df = pd.read_excel(filename, index_col=0)
    return df

def parameters_computation(df):
    mean_list = []
    var_list = []
    median_list = []

    for i in range(0,df.shape[0]):
        mean_list.append(np.mean(df.iloc[i,:]))
        var_list.append(np.var(df.iloc[i,:]))
        median_list.append(np.median(df.iloc[i,:]))
    return mean_list, var_list, median_list

def fig_plot(mean_list, var_list, median_list):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    ax1.hist(mean_list, bins=50)
    ax2.hist(var_list, bins=50)
    ax3.hist(median_list, bins=50)
    plt.show()
