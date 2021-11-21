# Task4.py 
# Code for Gauss Elimination and backsub. 

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
    print("Scaled matrix")
    printMtrx(mtrx)

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
        print("We swapped rows the following rows", diag, "and", maxIndex)




def printMtrx(mtrx):
    for row in mtrx:
        print(row)

def main():
    #Note this is  random digaonally dominant matrix
    A = [[1, -6, 12, -3],
           [-3, 2, 3, -9],
           [8, 1, -2, -3],
           [-1, -10, 2, 5]]
    # C = [[3, -2, 1],
    #         [1, -3, 2],
    #         [-1, 2, 4]]
    
    b = [1 for i in range(len(A))]
    
    # b2 = [1 for i in range(len(C))]

    print("Original matrix")
    printMtrx(A)
    EA, Eb = gaussElimScaledPartialPivot(A, b)
    print("Eliminated matrix with partial pivoting. ")
    printMtrx(EA)
    print("Eliminated col 1s")
    print(Eb)
    x = backsolve(EA, Eb)
    print("Sol x: ", x)
    
main()
    
    

