def initialize(size):
    mtrxA = []
    for i in range(size):
        new = []
        for j in range(size):
            if j >= i:
                num = i + 1 +j +1 -1
                new.append(num)
            if j < i:
                new.append(0)
        mtrxA.append(new)
    # print(mtrxA)
    return mtrxA

def transpose(mtrx):
    # mtrxT = mtrx[:][:]
    mtrxT = [[None for j in range(len(mtrx))] for j in range(len(mtrx))]
    # print(mtrxT)
    size = len(mtrx)
    for i in range(size):
        for j in range(size):
            mtrxT[i][j] = mtrx[j][i]
    return mtrxT



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



def main():
    size = 3
    A = initialize(size)
    print("This is A", A)
    AT = transpose(A)
    print("This is A^T: ", AT)
    vecB = [1 for j in range(size)]
    x = forwardSolve(AT, vecB)
    print("This is the solution to a column of 1s", x)



main()
    
