import math
from math import sin
from math import exp


import sys
sys.path.insert(0, '../lib/')

#from .lib.newtonRoot.py import newtonRoot
from bisection import bisection
#from .lib.funcIter.py import fixedPoint
#from .lib.secantRoot.py import secantRoot

def function(x):
    y = exp(-1 *(x * x)) * sin(4 * x *x - 1.0) + 0.051
    return y


def main():
    tol = 0.001
    bRoot = bisection(-.1, .8, function, tol)
    print(bRoot, "tolerance = ", tol)


main()
