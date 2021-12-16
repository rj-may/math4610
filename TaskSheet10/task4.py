import sys
sys.path.insert(0, '../lib/')

from matrix.vecNorms import lInfNorm
from matrix.diagDom import diagonallyDominant

def lInfMatrixNorm(matrix):
    size = len(matrix)
    norm = 0
    for i in range(size):
        testList = [None for j in range(size)]
        for j in range(size):
            testList[j] = matrix[i][j]
        testNorm = lInfNorm(testList)
        if testNorm > norm:
            norm = testNorm
    return norm

def main():
    matrix = diagonallyDominant() 
    norm = lInfMatrixNorm(matrix)
    print(norm)

main()