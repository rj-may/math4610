import math
from math import sin
from math import cos
from math import exp


def findSmallestRoot(func, df, maxIter, tol):
    h = .1
    iter = 0
    rootFound = False
    negRootFound = False
    array = []
    while(not rootFound):
        interval = h * iter
        negInterval = -1 * h * iter
        if func(interval) * func(0) < 0:
            rootFound = True
        if func(negInterval) * func(0) < 0:
            negRootFound = True
        iter += 1
    
    if(rootFound and negRootFound):
        if func(interval) == func(negInterval):
            print("Symmteric function around 0")
            array.append(hybridRoot(func, df, interval / 2 ,0, interval, maxIter, tol))
    else:
        if(rootFound):
            array.append(hybridRoot(func, df, interval / 2, 0, interval, maxIter, tol))
        if(negRootFound):
            array.append(hybridRoot(func, df, negInterval / 2, negInterval, 0, maxIter, tol))
    
    return array


def hybridRoot(func, df, x0, a, b, maxIter, tol):
    if abs(func(x0)) < tol: 
        return x0
    xNext = x0
    if func(a) * func(b) > 0: 
       return "Error, a and b values share the same sign "
    
    if (x0 < a or x0 > b):
        return "Error, initial guess is not in range of (a,b)"

    error = abs(func(x0))
    
    for i in range(maxIter):
        xNext = x0 - func(x0)/df(x0)
        errorNext = abs(xNext - x0)
        if errorNext < tol:
            return xNext #break with result
        #guarantees that the root we are getting closer to is between (a,b)
        if (errorNext > error or a > xNext or b < xNext ):  # got rid of error check
            ## do bisection 
            for i in range(4): # recommended iterations for bisection
                c = 1/2 * (a + b)
                if func(a) * func(c) < 0:
                    b = c
                else:
                    a = c
            error = abs(b- a)
            x0 = c        
        else:   
            x0 = xNext

    print("Max iterations reached, last x was", x0)



def func(x):
    y = exp(-1 *(x * x)) * sin(4 * x *x - 1.0) + 0.051
    return y

def df(x):
    dy = -2 * x*  exp(-1 *(x * x)) *( sin(4 * x *x - 1.0) - 4 * cos(4 * x * x - 1)) 
    return dy

def main():

    error = .001
    maxIter = 80
    print("Finding the smallest root of the function at with error %g and a max number of iterations of %d." %(error, maxIter))
    root = findSmallestRoot(func, df, maxIter, error)
    for r in root:
        print("Root: ", r)
    
main()

    
