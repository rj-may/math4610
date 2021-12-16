#Math 4610 Fundamentals of Computational Mathematics Software Manual File


**Routine Name:**           matrixOps: matrixAdd, matrixSub, transpose, scalarMatrix, matrixVecMult, matrixMult

**Author:** Riley May

**Language:** python

**Description/Purpose:** This program calculates various matrix operations.
These are basic linear algebra operations. I have double checked all the outups. 

**Input:** The input for all of these are arrays or two dimensional arrays. It doesn't check matrix addition and subtraction size. The multiplication operations perform checks to make sure your vectors or matrices are of the correct sizes.  Be careful with you inputs. 
Note that the first vector is multiplied first by the second. 
The scalar matrix multiplication is first the matrix then the scalar. 

**Output:** 

All of operations return two dimensional arrays except matrixVectMult. It is the 

**Usage/Example:**

Here is an example of the code working.     
It is fairly simple code. The exact code that was run is found in Task3 of Tasksheet 9, but the output explains what is going on. 
It has checks to make sure the dimensions work for the multiplication operations. 

    
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


**Implementation/Code** The following code is for  matrixOps.py

These are basic normal matrix operations. 

    def matrixAdd(A, B):
        C = [[None for k in range(len(A[0]))] for j in range(len(A))]
        if len(A) != len(B):
            return "Error"
        for i in range(len(A)):
            for j in range(len(A[i])):
                C[i][j] = A[i][j] + B[i][j]
        return C

    def matrixSub(A, B):
        C = [[None for k in range(len(A[0]))] for j in range(len(A))]
        if len(A) != len(B):
            return "Error"
        for i in range(len(A)):
            for j in range(len(A[i])):
                C[i][j] = A[i][j] - B[i][j]
        return C

    def transpose(mtrx):
        # mtrxT = mtrx[:][:]
        mtrxT = [[None for j in range(len(mtrx))] for j in range(len(mtrx[0]))]
        # print(mtrxT)
        # size = len(mtrx)
        for i in range(len(mtrxT)):
            for j in range(len(mtrxT[0])):
                mtrxT[i][j] = mtrx[j][i]
        return mtrxT

    def scalarMatrix(A, scalar):
        C = [[None for k in range(len(A[0]))] for j in range(len(A))]
        # print(C)
        for i in range(len(A)):
           for j in range(len(A[i])):
               C[i][j] = A[i][j] * scalar
        return C

    def matrixVectMult(A, x):
        b = [None for i in range(len(A))]
        if len(A[0]) != len(x):
            return "Sizes don't match"
        else:
            for i in range(len(A)):
                b[i] = dotProd(A[i], x)
            return b

    def matrixMult(A, B):
        C = [[None for k in range(len(A))] for j in range(len(B[0]))]
        if len(A[0]) != len(B):
            return "Incompatible matrix multiplication"
        else:
            col = [None for j in range(len(B))]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(col)): # this gets a column from B
                        col[k] = B[k][j] 
                    C[i][j] = dotProd(A[i], col)
            return C





**Last Modified:** December/2021
