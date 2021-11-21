# Task4.py 
# Code for Gauss Elimination and backsub
# This code uses scaled partial pivoting. 


def gaussElimScaledPartialPivot(mtrx, vecB):
    #first scale it to the value with the largest magnitude. 
    rowNum = 0 # I needed this because I couldn't get to the b vector without it. 
    for row in mtrx:
        scale = abs(row[0])
        for i in row:
            if abs(i) > abs(scale):
                scale = i
        for k in range(len(row)):
            row[k] = row[k] / scale
        vecB[rowNum] = vecB[rowNum] /scale
        rowNum += 1

    n = len(vecB)
    for k in range(0, n-1):
        partialPivot(mtrx, vecB, k)
        for i in range(k+1, n):
            factor = mtrx[i][k] / mtrx[k][k]
            for j in range(k, n):
                mtrx[i][j] -= (factor * mtrx[k][j]) 
            vecB[i] -= factor * vecB[k]
    
    return mtrx, vecB
    
def partialPivot(A, b, diag):
    n = len(b)
    maxIndex = diag #start with assuming the largest magnitude is at the diagonal
    for i in range(diag + 1, n):
        if abs(A[i][diag]) > abs(A[maxIndex][diag]): 
            maxIndex =  i
    if maxIndex != diag:
        # we need to do some row swapping
        #This here should work without returning anything becuase python is pass by reference.
        A[diag], A[maxIndex] = A[maxIndex], A[diag]
        b[diag], b[maxIndex] = b[maxIndex], b[diag]




    
