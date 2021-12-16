
import sys
sys.path.insert(0, '../lib/')

from matrix.vecNorms import l2Norm
from matrix.matrixOps import matrixVecMult
from matrix.vecOps import vecSub
from matrix.vecOps import vecAdd




def jacobi(matrix, b, x_k, tolerance, maxIter):  # x_k1 = x_k + D^-1(r_k)

    resid = vecSub(b, matrixVecMult(matrix, x_k))
    for i in range(maxIter):
        print("resid,", resid)
        if l2Norm(resid) < tolerance:
            return x_k
        DinvResid = []
        for entry in range(len(resid)):
            DinvResid.append((1/matrix[entry][entry])*resid[entry])
        print("DinvResid", DinvResid)
        x_k = vecAdd(x_k, DinvResid)
        print("new xK", x_k)
        test1 = matrixVecMult(matrix, x_k)
        print("test1 ", test1)
        print("b ", b)
        resid = vecSub(b, test1 )
        print("resid 2 = b - test1")
        print("resid2, ", resid)
    return x_k


def main():
    matrix = [[3, 1, 1, 0],
              [0, 2, 1, 0],
              [0, 0, 2, 1],
              [0, 0, 0, 1]]
    b = [5, 3, 3, 1]
    tolerance = .001
    maxIter = 1
    x0 = [5, 10, 6, 20]

    print(jacobi(matrix, b, x0, tolerance, maxIter))

main()
