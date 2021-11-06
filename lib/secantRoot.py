import math

def secantRoot(func, x0, x1, maxIter, tol):
    if abs(func(x0)) < tol: 
        return x0
    for i in range(maxIter):
        x2 = x1 - func(x1) * (x1 - x0)/ (func(x1)- func(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2 # reassigning variables. 

    print("Max iterations reached. ")


# def func(x):
#     return ( (x * math.exp(3 * x * x)) - (7 * x) )
# def main():
#     x0 = .6
#     x1 = .9
#     error = .001
#     maxIter = 80
#     print("Funciton with starting x0 = %f, x1 = %f, with an error of %f and a max number of iterations of %d" %(x0, x1, error, maxIter))
#     root = secantRoot(func, x0, x1, maxIter, error)
#     print("Root: ", root)
# main()
   
