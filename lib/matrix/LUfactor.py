

## LU factorization for square matrix
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