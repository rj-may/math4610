# import some stuff
# -----------------
#
from matplotlib import pyplot as plt
import numpy as np
#

def graphFunc(*args):
    for arg in args:
        xVal = []
        yVal = []
        for i in range(-20, 21):
            xVal.append(i)
            eq = arg.replace("x", str(i))
            y = eval(eq)
            yVal.append(y)
        plt.plot(xVal, yVal, label = arg)
    plt.legend()
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()

def run():
    graphFunc(".5 * (x-5)**2 + 3",  " 20 * x")

run()
