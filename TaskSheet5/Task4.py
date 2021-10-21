import math
from matplotlib import pyplot as plt
from math import log10 as log

def secantRoot(func, x0, x1, maxIter, tol):
    if abs(func(x0)) < tol: 
        return "Already a root."
    error = tol * 10 #Initial error
    #lists for the log of our error at the k and the k + 1 case
    err_k = [] 
    err_kplus1 = []
    for i in range(maxIter):
        x2 = x1 - func(x1) * (x1 - x0)/ (func(x1)- func(x0))
        err_k.append(log(error))
        error = abs(x2 - x1)
        err_kplus1.append(log(error))
        if abs(error) < tol:
            break #if we are in our tolerance range, stop
        x0, x1 = x1, x2 # reassigning variables. 

    return err_k, err_kplus1


def func(x):
    return ( (x * math.exp(3 * x * x)) - (7 * x) )


def main():
    x0 = .6
    x1 = .9
    tol = .0001
    maxIter = 80
    print("Funciton with starting x0 = %f, x1 = %f, with an tolerance of %f and a max number of iterations of %d" %(x0, x1, tol, maxIter))
    x, y = secantRoot(func, x0, x1, maxIter, tol)
    print(len(x), "= Len of x, which is equivalent to number of iterations")
    plt.plot(x, y)
    plt.legend()
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title("Log-Log plot of error of Secant Method")
    plt.show()
    
main()

    
