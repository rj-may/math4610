# Here is the code for a fixed point iteratioin.


# fx is funciton of x, tol is for the tolerance,  maxIter is max iterations
def fixedPoint(x0, fx, tol =.1 , maxIter = 100):
    iter = 0
    error = 10 * tol
    while(error > tol and iter < maxIter):
        x1 = x0 - fx(x0)  #g(x) is defined to be x - f(x)
        error = abs(x1 - x0)
        x0 = x1
        iter += 1
        #print(iter)
    if iter == maxIter:
        return "No root found in " + str(iter) +  " iterations. The was the last value: " + str(x0)
    else:
        return str(x0) +  " at  " + str(iter) + "  iterations."
