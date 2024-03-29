import math
from matplotlib import pyplot as plt
from math import log10 as log

def newtonRoot(func, df, x0, maxIter, tol):
    iter = 0
    if abs(func(x0)) < tol: 
        return "Already a root"
    err_k = []
    err_kplus1 = []
    error = 10* tol
    while (error > tol and iter < maxIter):
        err_k.append(log(error))
        xNext = x0 - func(x0)/df(x0)
        error = abs(xNext - x0)
        err_kplus1.append(log(error))
        iter += 1
        x0  = xNext
    return err_k, err_kplus1


def func(x):
    return ( (x * math.exp(3 * x * x)) - (7 * x) )

def df(x):
    return (math.exp(3 * x * x) + 6 * x * x * math.exp(3 * x * x)-7)


def main():
    x1 = .7
    tolerance = .001
    maxIter = 80
    print("Funciton with starting x = %f with an tolerance of %f and a max number of iterations of %d" %(x1, tolerance, maxIter))
    x, y = newtonRoot(func, df, x1, maxIter, tolerance)
    plt.plot(x, y)
    plt.legend()
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title("Log-Log plot of error of Netwon's Method")
    plt.show()

main()

    
