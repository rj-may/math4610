#Tasksheet 4 Task 5
from math import log2
from math import ceil
import math # this is for any functions that we pass into it. 


def bisection(a, b, func, tol):
    fa = func(a)
    fb = func(b)
    if (fa * fb > 0): return "No root in [a,b] or f(a) and f(b) have the sign."
    e0 = abs(b -a) #initial error
    k = ceil(log2(e0/tol)) #This is the number of iterations we will do. Round up to ensure it works. 

    for i in range(k):
        c = .5 * (a + b)
        fc = func(c)
        if (fa * fc < 0):
            b =c 
            fb = fc
        else:
            a = c
            fa = fc

    return c 



def funky(x):
    return ( (x * math.exp(3 * x * x)) - (7 * x) )


def main():
    start1 = -.25
    end1 = .25
    tol1 = .005
    print("Bisection with x values, {:f}, {:f}, tolerance of {:f}".format( start1, end1, tol1))
    val1 = bisection(start1, end1, funky, tol1)
    print("The root is:  ", val1)
    print()
    start2 = .725 
    end2 = .825
    tol2 = 0.005
    print("Bisection with x values,{:f} , {:f}, tolerance of {:f}".format(start2, end2, tol2))
    val2 = bisection(start2, end2, funky, tol2)
    print("The root is:  ", val2)


main()
