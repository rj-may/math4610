import math
from math import sin
from math import cos
from math import exp


import sys
sys.path.insert(0, '../lib/')

from newtonRoot import newtonRoot


def function(x):
    y = exp(-1 *(x * x)) * sin(4 * x *x - 1.0) + 0.051
    return y

def df(x):
    dy = -2 * x*  exp(-1 *(x * x)) *( sin(4 * x *x - 1.0) - 4 * cos(4 * x * x - 1)) 
    return dy

def main():
    tol = 0.001
    maxIter = 100
    x0 = -5
    print("x0= ", x0, ". Tol = ", tol)
    nRoot = newtonRoot(function, df, x0, maxIter, tol)
    print("Newton root: ", nRoot)


    print()
    x0 = .6
    print("x0= ", x0, ". Tol = ", tol)
    nRoot = newtonRoot(function, df, x0, maxIter, tol)
    print("Newton root: ", nRoot)
    
main()
