#Math 4610 Fundamentals of Computational Mathematics Software Manual T

**Routine Name:**           backsolve.py

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will compute the solution of an  system of Ly=b. It is great for solving 
systems of linear equations. 

**Input:** A matrix (2 dimensional list), and a vector (list). The matrix should be a lower triangular matrix

**Output:** This code outputs a vector or a list. 

**Usage/Example:**

This function needs two parameters to work. 
It takes a Lower matrix of any size with its accompanying vector b. This is is great for solving Ly=b


This is an example of the code that of the forward solving function. 

This is A^T:  [[1, 0, 0], [2, 3, 0], [3, 4, 5]]       
This is the solution to a column of 1s [1.0, -0.3333333333333333, -0.13333333333333336]

**Implementation/Code:** The following is the code for fowardsolve()


def forwardSolve(mtrx, vecB):
    n = len(vecB)
    vecX = [None for i in range(n)]
    m = n -1
    vecX[0] = vecB[0] / mtrx[0][0]
    for i in range(1, n):
        summation = vecB[i]
        for j in range(0, i):
            summation -= ( mtrx[i][j] * vecX[j])
        vecX[i] = summation / mtrx[i][i]
    return vecX

**Last Modified:** Nov 2021
