#  running the function   fixed point iteration 
import math
import Task3


fixPtIter = Task3.fixedPoint

def funkyFunc(x):
    return ( (x * math.exp(3 * x * x)) - (7 * x) )


def epsFunc(x):
    return  2 /(math.exp(3 * x * x) + 6 * x * x * math.exp(3 * x * x)-7)   * (x * math.exp(3 * x * x) - (7 * x))

def main():
    start = .8 
    tol = .01
    maxIter = 100 
    ans = fixPtIter(start, epsFunc, tol, maxIter)
    print("This function started at x= ", start, ". The tolerance was ", tol, ". The max iterations was ", maxIter, ". ")
    print("The first root found was", ans)


main()

