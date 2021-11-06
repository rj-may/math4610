import math

def newtonRoot(func, df, x0, maxIter, err):
    if abs(func(x0)) < err: 
        return x0
    xNext = x0
    for i in range(maxIter):
        xNext = x0 - func(x0)/df(x0)
        if abs(xNext - x0) < err:
            return xNext #break with result
        x0 = xNext

    print("Max iterations reached. ")

# def func(x):
#     return ( (x * math.exp(3 * x * x)) - (7 * x) )

# def df(x):
#     return (math.exp(3 * x * x) + 6 * x * x * math.exp(3 * x * x)-7)
# def main():
#     x1 = .7
#     error = .001
#     maxIter = 80
#     print("Funciton with starting x = %f with an error of %f and a max number of iterations of %d" %(x1, error, maxIter))
#     root = newtonRoot(func, df, x1, maxIter, error)
#     print("Root: ", root)
   
# main()    
