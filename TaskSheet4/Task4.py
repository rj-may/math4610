#  running the function   fixed point iteration 
import math
import Task3


fixPtIter = Task3.fixedPoint

def funkyFunc(x):
    return ( (x * math.exp(3 * x * x)) - (7 * x) )


def main():
    start = 0
    tol = .1
    maxIter = 20 
    ans = fixPtIter(start, funkyFunc, tol, maxIter)
    print("This function started at x= ", start, ". The tolerance was ", tol, ". The max iterations was ", maxIter, ". ")
    print("The first root found was", ans)


main()

