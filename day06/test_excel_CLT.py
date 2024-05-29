import pandas as pd
import numpy as np
from functions import input_file, parameters_computation

def test_parameters_computation_1():
    df= input_file('test_Statistics_data.xlsx')
    mean_list, var_list, median_list = parameters_computation(df)
    assert round(mean_list[0], 3) == 0.931

def test_parameters_computation_2():
    df= input_file('test_Statistics_data.xlsx')
    mean_list, var_list, median_list = parameters_computation(df)
    assert round(var_list[0], 3) == 0.846
    
def test_parameters_computation_3():
    df= input_file('test_Statistics_data.xlsx')
    mean_list, var_list, median_list = parameters_computation(df)
    assert round(median_list[0], 3) == 0.669

