import matplotlib.pyplot as plt
import math
from math import cos

#import stuff from Task1 
xVal = 2

def secDerivApprox(x, h):
    approximation = (cos(x + h) - 2 * cos(x) + cos(x - h)) / (h **  2)
    return approximation



def main():
    actual = -cos(xVal)
    hVal = []
    error = []
    # print(format("h", "<6") + format("\t -cos(2)", "<25") + format("Central diff Approx ", "<24") + format("Difference", "<20"))
    for i in range(-1,17):
        if i == -1:
            h = 1
            approx = secDerivApprox(xVal, h)
            error.append(abs(approx - actual))
        elif i == 0:
            h = 0.5
            approx = secDerivApprox(xVal, h)
            error.append(abs(approx - actual))
        else:
            h = 1 * (10 ** (-1 * i))
            approx = secDerivApprox(xVal, h)
            error.append(abs(approx - actual))

        hVal.append(h)

    # convert the lists for a log log plot
    # 14 is used because the code breaks find the log of 0

    for i in range(len(hVal)):
        hVal[i] = math.log(hVal[i])
        error[i] = math.log(error[i])
    



    plt.plot(hVal, error)
    plt.xlabel("log of h")
    plt.ylabel("log of error")
    plt.title("The title ")

    plt.show()

main()
