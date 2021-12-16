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

    x = [1, 2, 3]
    y =  [4, 5, -6, 7]
    z =  [2, -3, 1]
    l1 norm of y=  22
    l2 norm of x= 3.7416573867739413
    l infinity norm of z= -3
    L1 Norm error of x, z = 8
    L2 Norm error of x, z = 5.477225575051661
    L infinity Norm error of x, z = 5




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
