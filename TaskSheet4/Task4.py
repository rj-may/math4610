#  running the function   fixed point iteration 
import math
import Task3


fixPtIter = Task3.fixedPoint

#this funcition breaks because of math overflow  eror. 
def funkyFunc(x):
    return ( (x * math.exp(3 * x * x)) - (7 * x) )

#here is the value of epsilon times the f(x) or funkyFunc. 
# epsilon was determined to be 2 / f'(x).  This was determined by solving (g'(x)) <= 1 where g(x) = x - f(x)
def epsFunc(x): 
    return  2 /(math.exp(3 * x * x) + 6 * x * x * math.exp(3 * x * x)-7)   * (x * math.exp(3 * x * x) - (7 * x))

def run(start, tolerance):
    maxIter = 200 
    ans = fixPtIter(start, epsFunc, tolerance, maxIter)
    print("This function started at x= ", start, ". The tolerance was ", tolerance, ". The max iterations was ", maxIter, ". ")
    print("The root found was", ans)

def main():
	run(0, 0.02)
	run(.5, 0.02)
	run(.8, 0.01)


main()

