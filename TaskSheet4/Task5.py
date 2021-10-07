#Tasksheet 4 Task 5
from math import log10
from math import ceil
import math # this is for any functions that we pass into it. 


def bisection(a, b, func, tol):
    fa = func(a)
    fb = func(b)
    if (fa * fb < 0): return "No root in [a,b] or f(a) and f(b) have the sign."
    e0 = abs(b -a) #initial error
    k = ceil(log10(e0/tol)/log10(2)) #This is the number of iterations we will do. Round up to ensure it works. 


    for i in range(k):
        c = .5 (a * b)
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
    print("Bisection with starting, 0, 0, tolerance of .05")
    val1 = bisection(0, 0, funky, .05)
    print("The root is;  ", val1)
    print()
    print("Bisection with starting, .5, 1, tolerance of .05")
    val2 = bisection(.5, 1, funky, .05)
    print("The root is;  ", val2)
