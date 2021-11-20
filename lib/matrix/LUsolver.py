
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
    L, U = LUfactor(mtrx)
    #solve  Ly = b
    y = forwardSolve(L, b)
    x = backsolve(U, y)
    return x