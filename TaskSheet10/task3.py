import sys
sys.path.insert(0, '../lib/')

from matrix.vecNorms import l1Norm
from matrix.diagDom import diagonallyDominant


def l1MatrixNorm(matrix):
    size = len(matrix)
    norm = 0
    for i in range(size):
        testList = [None for j in range(size)]
        for j in range(size):
            testList[j] = matrix[i][j]
        testNorm = l1Norm(testList)
        if testNorm > norm:
            norm = testNorm
    return norm

def main():
    matrix = diagonallyDominant() 
    norm = l1MatrixNorm(matrix)
    print(norm)

main()