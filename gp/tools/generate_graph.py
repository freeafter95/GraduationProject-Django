#_*_coding:utf-8_*_

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

def gs_graph(result, path):
    xs = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
    y1 = [random.randint(10, 80) for i in range(14)]
    y2 = [random.randint(15, 30) for i in range(14)]
    y3 = [random.randint(0, 60) for i in range(14)]

    plt.title('Computition Graph')
    plt.plot(xs, y1, color='green', label='irr_nyqfl')
    plt.plot(xs, y2, color='red', label='irr_nyppl(/10)')
    plt.plot(xs, y3, color='blue', label='irr_rpzxs(/10)')
    plt.legend()
    plt.xlabel('Fe')
    plt.ylabel('Attrs')
    plt.savefig(path)


