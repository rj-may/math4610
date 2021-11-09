import math
from math import sin
from math import cos
from math import exp


# import sys
# sys.path.insert(0, '../lib/')

# from newtonRoot import newtonRoot
from lib import bisection
# from funcIter import fixedPoint
# from secantRoot import secantRoot

def function(x):
    y = exp(-1 *(x * x)) * sin(4 * x *x - 1.0) + 0.051
    return y

def df(x):
    dy = -2 * x*  exp(-1 *(x * x)) *( sin(4 * x *x - 1.0) - 4 * cos(4 * x * x - 1)) 
    return dy

def main():
    tol = 0.001
    lBound, uBound = -.1, .8
    print("Bounds [", lBound,",", uBound, "] and tolerance = ", tol)
    bRoot = bisection(lBound, uBound, function, tol)
    print("Bisecion root: ", bRoot)
    print()
    x0 = -1
    maxIter = 200
    print("x0= ", x0, ". Tol = ", tol)
    fRoot = fixedPoint(x0, function, tol, maxIter)
    print("Functional iteration: ", fRoot)
    print()
    maxIter = 100
    x0 = .2
    x1 = .5
    print("x0= ", x0, ", x1 =", x1, ". Tol = ", tol)
    sRoot = secantRoot(function, x0, x1, maxIter, tol) 
    print("Secant root: ", sRoot)
    print()
    print("x0= ", x0, ". Tol = ", tol)
    nRoot = newtonRoot(function, df, x0, maxIter, tol)
    print("Newton root: ", nRoot)
    

main()
