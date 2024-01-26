import os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

input_y = [5, 7, 9, 6, 10]
input_x = [1, 2, 3, 4, 5]
output_function = None
degree = 3

def Power_Series():
    return np.polynomial.polynomial.Polynomial.fit(x = data_x, y = data_y, deg = degree)

if __name__ == '__main__':
    data_y = np.array(input_y)
    data_x = np.array(input_x)

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