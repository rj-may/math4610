import sys
sys.path.insert(0, '../lib/')

from matrix.vecNorms import l2Norm
from matrix.diagDom import diagonallyDominant


def l2MatrixNorm(matrix):
    size = len(matrix)
    norm = 0
    for i in range(size):
        testList = [None for j in range(size)]
        for j in range(size):
            testList[j] = matrix[i][j]
        testNorm = l2Norm(testList)
        if testNorm > norm:
            norm = testNorm
    return norm

def main():
    matrix = diagonallyDominant() 
    norm = l2MatrixNorm(matrix)
    print(norm)

main()