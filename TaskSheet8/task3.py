

'''
Task1.py 
Code for Gauss Elimination and backsub. 
Performed on diagonally dominant matrix
'''


def LUfactor(mtrx):
    n = len(mtrx)
    lower = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        lower[i][i] = 1
    for k in range(0, n-1):
        for i in range(k+1, n):
            factor = mtrx[i][k] / mtrx[k][k]
            for j in range(k, n):
                mtrx[i][j] -= (factor * mtrx[k][j]) 
            lower[i][k] = factor
            
    return lower, mtrx


def printMtrx(mtrx):
    for row in mtrx:
        print(row)

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


def backsolve(mtrx, vecB):
    n = len(vecB)
    vecX = [0 for i in range(n)]
    m = n - 1
    vecX[m] = vecB[m] / mtrx[m][m]
    for i in range(m -1,-1, -1,): #start at m-1, second to last entry, we want to include the 0th entry, -1 is indexing backward
        summation = vecB[i]
        for j in range(i+1, n):
            
            summation = summation - mtrx[i][j] * vecX[j]
        vecX[i] = summation / mtrx[i][i]
    return vecX

def LUsolver(mtrx, b):
    # print("Original matrix")
    # printMtrx(mtrx)
    L, U = LUfactor(mtrx)
    # print("Lower = ")
    # printMtrx(L)
    # print("Upper = ")
    # printMtrx(U)
    #solve  Ly = b
    y = forwardSolve(L, b)
    print("Intermediate step Forward solve Ly = b")
    print("y = ", y)
    print("Final solve Ux = y")
    x = backsolve(U, y)
    print("Sol x = ", x)
    return x

def hilbertMatrix(size):
    hilbert = [[None for i in range(size)] for k in range(size)]
    for i in range(size):
        for k in range(size):
            hilbert[i][k] = 1 / ( (i+1) + (k+1)  -1)

    b =[1 for k in range(size)]
    return hilbert, b

def main():
    for i in range(4, 11):
        print("Hilbert size = ", i, " x ", i)
        A, b = hilbertMatrix(i)
        LUsolver(A, b)

    

main()
    
    

