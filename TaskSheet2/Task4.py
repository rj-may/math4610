'''
Determine the order of accuracy of the central difference approximation of the second derivative.
'''
from math import cos

xVal = 2

def secDerivApprox(x, h):
    approximation = (cos(x + h) - 2 * cos(x) + cos(x - h)) / (h **  2)
    return approximation



def printDifferenceTable(h, actual, approx):
    diff = abs(actual - approx)
    h_sci_not = "{:.1e}".format(h)
    print(str(h_sci_not) + "\t " + str(actual) + "\t" + format(str(approx), "<20") + "\t" + str(diff))


def main():
    actual = -cos(xVal)
    print(format("h", "<6") + format("\t -cos(2)", "<25") + format("Central diff Approx ", "<24") + format("Difference", "<20"))
    for i in range(-1,17):
        if i == -1:
            h = 1
            approx = secDerivApprox(xVal, h)
            printDifferenceTable(h, actual, approx)
        elif i == 0:
            h = 0.5
            approx = secDerivApprox(xVal, h)
            printDifferenceTable(h, actual, approx)
        else:
            h = 1 * (10 ** (-1 * i))
            approx = secDerivApprox(xVal, h)
            printDifferenceTable(h, actual, approx)

        
        

main()



    
