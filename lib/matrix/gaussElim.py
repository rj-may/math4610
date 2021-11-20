#Gaussian elimination


def gaussElim(mtrx, vecB):
    n = len(vecB)
    for k in range(0, n-1):
        for i in range(k+1, n):
            factor = mtrx[i][k] / mtrx[k][k]
            for j in range(k, n):
                mtrx[i][j] -= (factor * mtrx[k][j]) 
            vecB[i] -= factor * vecB[k]
    
    return mtrx, vecB
