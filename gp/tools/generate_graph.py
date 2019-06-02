#_*_coding:utf-8_*_

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def gs_graph(result, path):
    xs = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
    y1 = [5, 7,8, 9,14,18,17,10,9,6,4,3,3,3]
    y2 = [10, 9,9,8,8,8,7,7,8,8,9,9,9,10]
    y3 = [13.2, 13.5, 13.3, 13.8, 14.1, 13.4, 13.6, 13.0, 12.8,13.3, 13.7, 13.9, 13.2, 13.6]

    plt.title('Computition Graph')
    plt.plot(xs, y1, color='green', label='irr_nyqfl')
    plt.plot(xs, y2, color='red', label='irr_nyppl(/10)')
    plt.plot(xs, y3, color='blue', label='irr_rpzxs(/10)')
    plt.legend()
    plt.xlabel('Fe')
    plt.ylabel('Attrs')
    plt.savefig(path)


