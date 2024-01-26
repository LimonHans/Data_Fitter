import os
import sys
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

input_x = [1, 2, 3, 4, 5, 6, 7]
input_y = [5, 7, 9, 6, 10, 36, 45]
data_names = []
output_function = None
degree = 3

def Power_Series():
    return np.polynomial.polynomial.Polynomial.fit(x = data_x, y = data_y, deg = degree)

if __name__ == '__main__':
    #file_path = sys.argv[1]
    file_path = r"D:\00workspace\nowfile\Data_Fitter\Test.xlsx"
    #file_dir, file_name = os.path.split(file_path)
    data_file = pd.read_excel(file_path)
    data_names = list(data_file.columns)
    
    input_x = list(data_file[data_names[0]])
    data_x = np.array(input_x)

    for y_id in range(1, len(data_names)):
        data_y = np.array(input_y)

        output_function = Power_Series()

        print(str(output_function))
        plt.scatter(data_x, data_y)
        data_x_max, data_x_min = max(data_x), min(data_x)
        data_x_ext_dis = 0.3*(data_x_max - data_x_min)
        data_x_ext_num = round(0.3*len(data_x))
        data_x_ext = np.append(np.append(
            np.linspace(data_x_min - data_x_ext_dis, data_x_min, data_x_ext_num),
            data_x),
            np.linspace(data_x_max, data_x_max + data_x_ext_dis, data_x_ext_num))
        plt.plot(data_x_ext, output_function(data_x_ext))
    plt.show()