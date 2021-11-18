#This is the Task5 code
from random import randint

def createMatrix(dim):
    rangeNum = 10
    mtrx = [[None for i in range(dim)] for k in range(dim)]
    for i in range(dim):
        for j in range(dim):
            mtrx[i][j] = randint(1, rangeNum)

    return mtrx


def gaussElim(mtrx, vecB):
    n = len(vecB)
    for k in range(0, n-1):
        for i in range(k+1, n):
            factor = mtrx[i][k] / mtrx[k][k]
            for j in range(k, n):
                mtrx[i][j] -= (factor * mtrx[k][j]) 
            vecB[i] -= factor * vecB[k]
    
    return mtrx, vecB


def main():
    size = 4
    A = createMatrix(size)
    printMtrx(A)
    b = [1 for i in range(size)]
    EA, Eb = gaussElim(A, b)

    print("A After performing Gaussian Elimination")
    printMtrx(EA)
    print("Vector b after performing Gaussian elim (note b was col 1s)")
    print(Eb)


def printMtrx(mtrx):
    for row in mtrx:
        print(row)

main()


