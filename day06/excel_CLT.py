import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions import input_file, parameters_computation, fig_plot

def main():

    df= input_file('Statistics_data.xlsx')
    mean_list, var_list, median_list = parameters_computation(df)
    fig_plot(mean_list, var_list, median_list)

main()



