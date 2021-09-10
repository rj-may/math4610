'''
Determine the order of accuracy of the central difference approximation of the second derivative.
'''
from math import cos

xVal = 2

def secDerivApprox(x, h):
    approximation = (func(x, h) - 2 * func(x) + func(x - h)) / (h * h)
    return approximation, h

def func(num):
    return cos(num)

def printDifferenceTable(h, actual, approx):
    diff = math.abs(actual - approx)
    h = h.tostring()
    h_sci_not = "{:e}".format(h)
    print(h + "\t" + actual + "\t" + approx + "\t" + diff)


def main():
    for i in range(0,17):
        hVal = 1 ** 


main()



    
