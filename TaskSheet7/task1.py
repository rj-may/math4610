
##this method creates a matrix of a given size and each entry on the diagonal or gerater = i + j -1
# it also returns a vector or array of b.
def initialize(size):
    array = [0 for i in range(size)]
    mtrxA = []
    for k in range(size):
        mtrxA.append(array)
    print(mtrxA)
    for row in mtrxA:
        i = 1
        for col in row:
            j=1
            if j >= i:
                row[j-1] = i  + j -1
            if j < i:
                row[j-1] = 0
            j+=1
        i+=1

    vecB = [1 for i in range(size)]
    print(mtrxA)
    print(vecB)
    return mtrxA, vecB

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


def main():
    dim = 3
    print("The matrix dim =", dim)
    A, b = initialize(dim)
    x = backsolve(A, b)
    print(x)

main()
