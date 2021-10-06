# import some stuff
# -----------------
#
from matplotlib import pyplot as plt
import numpy as np
#

def graphFunc(args):

    for arg in args:
        xVal = []
        yVal = []
        for i in range(-21, 21):
            xVal.append(i)
            eq = arg.replace("x", i)
            y = eval(eq)
            yVal.append(y)
        plt.plot(xVal, yVal)
    plt.show()
