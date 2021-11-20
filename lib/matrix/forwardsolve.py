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