# Task 4
from random import randint


def createDiagMtrx(dim):
    rangeNum = 10
    mtrx = [[0 for i in range(dim)] for k in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if (i == j):
                mtrx[i][i] = randint(1, rangeNum)
    return mtrx


def printMtrx(mtrx):
    for row in mtrx:
        print(row)

def main():
    D = createDiagMtrx(4)
    printMtrx(D)

main()
