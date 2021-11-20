'''
Task1.py 
Code for Gauss Elimination and backsub. 
Performed on diagonally dominant matrix
'''

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



def gaussElim(mtrx, vecB):
    n = len(vecB)
    for k in range(0, n-1):
        for i in range(k+1, n):
            factor = mtrx[i][k] / mtrx[k][k]
            for j in range(k, n):
                mtrx[i][j] -= (factor * mtrx[k][j]) 
            vecB[i] -= factor * vecB[k]
    
    return mtrx, vecB


def printMtrx(mtrx):
    for row in mtrx:
        print(row)

def main():
    #Note this is  random digaonally dominant matrix
    A = [ [8, 1, -2, -3],
            [-1, -10, 2, 5],
            [1, -6, 12, -3],
            [-3, 2, 3, -9]]
    C = [[3, -2, 1],
            [1, -3, 2],
            [-1, 2, 4]]
    
    b = [1 for i in range(len(A))]
    
    b2 = [1 for i in range(len(C))]

    print("Original matrix")
    printMtrx(A)

    EA, Eb = gaussElim(A, b)
    print("Eliminated matrix")
    printMtrx(EA)
    print("Eliminated col 1s")
    print(Eb)
    x = backsolve(EA, Eb)
    print("Sol x: ", x)
main()
    
    

