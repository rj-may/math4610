from random import randint


def createMatrix(dim):
    rangeNum = 10
    mtrx = [[None for i in range(dim)] for k in range(dim)]
    for i in range(dim):
        for j in range(dim):
            mtrx[i][j] = randint(rangeNum * -1, rangeNum)
    return mtrx

def createUpper(dim):
    rangeNum = 10
    mtrx = [[None for i in range(dim)] for k in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if j >= i:
                mtrx[i][j] = randint(rangeNum * -1, rangeNum)
            else:
                mtrx[i][j] = 0
    return mtrx

def createLower(dim):
    rangeNum = 10
    mtrx = [[None for i in range(dim)] for k in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if j <= i:
                mtrx[i][j] = randint(rangeNum * -1, rangeNum)

            else:
                mtrx[i][j] = 0
    return mtrx

def main():
    print("Note these are assigned valules -10 to 10")
    sq = createMatrix(4)
    print("This is the square matrix")
    printMtrx(sq)
    mtrxU = createUpper(3)
    print("This is the upper triangular matrix")
    printMtrx(mtrxU)

    mtrxL = createLower(3)
    print("This is the lower matrix:")
    printMtrx(mtrxL)
    


def printMtrx(mtrx):
    for row in mtrx:
        print(row)

main()
