import math

def hybridRoot(func, df, x0, a, b, maxIter, tol):
    if abs(func(x0)) < tol: 
        return x0
    xNext = x0
    if func(a) * func(b) > 0: 
        return "Error, a and b values are on opposite sides "
    
    if (x0 < a or x0 > b):
        return "Error, initial guess is not in range of (a,b)"

    error = abs(func(x0))
    
    for i in range(maxIter):
        xNext = x0 - func(x0)/df(x0)
        errorNext = abs(xNext - x0)
        if errorNext < tol:
            return xNext #break with result
        if (errorNext > error or a > xNext or b < xNext ): #guarantees that the root we are getting closer to is between (a,b)
            ## do bisection 
            for i in range(4): # recommended iterations for bisection
                c = 1/2 * (a + b)
                if func(a) * func(c) < 0:
                    b = c
                else:
                    a = c
            print("Bisection was performed")
            error = abs(b- a)
            x0 = c        
        else:   
            x0 = xNext

    print("Max iterations reached. ")



def func(x):
    return ( (x * math.exp(3 * x * x)) - (7 * x) )

def df(x):
    return (math.exp(3 * x * x) + 6 * x * x * math.exp(3 * x * x)-7)


def main():
    a = .2
    b = 1.5
    x0 = .5
    error = .001
    maxIter = 80
    print("Funciton with starting x = %g with an error of %g and a max number of iterations of %d. With range of a and b being %g, %g" %(x0, error, maxIter, a, b))
    root = hybridRoot(func, df, x0, a, b, maxIter, error)
    print("Root: ", root)
    
main()

    
