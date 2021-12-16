#Math 4610 Fundamentals of Computational Mathematics Software Manual File


**Routine Name:**           vecNorms: l1Norm, l2Norm, LInfNorm, l1NormErr, l2NormErr, lInfNormErr

**Author:** Riley May

**Language:** python

**Description/Purpose:** This program calculates various norms.  operations.  The included vector norms are the L1 norm, the L2 norm, the L infinity norm, and errors for each of those. 

**Input:** The input for the L1, L2 and Linfinty norms are all vectors. 
The input for all of the error functions are two vectors of the same size. 


**Output:** 

All of the vector operations willl return a single numerical value. 


**Usage/Example:**

Here is an example of the code working.     
It is fairly simple code. The exact code that was run is found in Task2 of Tasksheet 9, but the output explains what is going on. 

    
    A = 
    [1, 2, 3]
    [4, 5, 6]
    B = 
    [2, 1, 2]
    [2, 3, 1]
    A + B =
    [3, 3, 5]
    [6, 8, 7]
    A - B =
    [-1, 1, 1]
    [2, 2, 5]
    Scalar multiplier:  3
    E = A * 4
    [3, 6, 9]
    [12, 15, 18]
    E transpose
    [3, 12]
    [6, 15]
    [9, 18]
    Vec x =  [2, 1, 1]
    Ax = 
    [7, 19]
     A * B^T = 
    [10, 11]
    [25, 29]


**Implementation/Code** The following code is for  vecNorms.py

These are basic vector normal operations. 

    def l1Norm(x):
        norm = 0
        for i in range(len(x)):
            norm += abs(x[i])
        return norm


    def l2Norm(x):
        normsqd = 0
        for i in range(len(x)):
            normsqd += x[i] * x[i]
        norm = normsqd ** (1/2)
        return norm

    def lInfNorm(x):
        norm = 0
        for i in range(len(x)):
            if abs(x[i]) > abs(norm):
                norm = x[i]
        return norm

    def subtract(x, y):
        if len(x) != len(y):
            return "error in vector size"
        err = [None for i in range(len(x))]
        for i in range(len(x)):
            err[i] = x[i] - y[i]
        return err

    def l1NormErr(x, y):
        e = subtract(x, y)
        return l1Norm(e)

    def l2NormErr(x, y):
        e = subtract(x, y)
        return l2Norm(e)

    def lInfNormErr(x, y):
        e = subtract(x, y)
        return lInfNorm(e)






**Last Modified:** December/2021
