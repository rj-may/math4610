# Here is the code for a fixed point iteration.

# fx is funciton of x, maxIter is max iterations
def fixedPoint(x0, fx, tol, maxIter):
    iter = 0
    error = 10 * tol
    while(error > tol and iter < maxIter):
        x1 = fx(x0)
        error = abs(x1 - x0)
        x0 = x1
        iter += 1
    return x1
