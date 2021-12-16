import sys
sys.path.insert(0, '../lib/')

from matrix.vecNorms import l1Norm
from matrix.vecNorms import l2Norm
from matrix.vecNorms import lInfNorm


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
