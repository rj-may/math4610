
import sys
sys.path.insert(0, '../lib/')

from matrix.vecNorms import l2Norm
from matrix.matrixOps import matrixVecMult
from matrix.vecOps import vecSub
from matrix.vecOps import vecAdd





# def jacobiIteration(A, b, x0, tol, maxIter):
#     n = len(b)
#     error = 10 * tol
#     iter = 0
#     r = [None for i in range(len(x0))]
#     x1 = [None for i in range(len(x0))]
#     while(error > tol and iter < maxIter):
#         # Residual 
#         for i in range(n):
#             r[i] = b[i]
#             for j in range(n):
#                 r[i] = r[i] - A[i][j]* x0[j]
#         # Update
#         for i in range(n):
#             x1[i] = x0[i] - r[i]/ A[i][i]
#         error = l2NormErr(b, matrixVectMult(A, x1))
#         iter += 1
#         for i in range(n):
#             x0[i] = x1[i]
#         if error < tol:
#             return x1
#     if iter ==  maxIter:
#         print("no solution reached", x1)
#         return "Maxiterations was reached. "
        

# # page 4 https://www3.nd.edu/~zxu2/acms40390F12/Lec-7.3.pdf
# def jacobiIteration(A, b, x0, tol, maxIter):
#     n = len(b)
#     error = 10 * tol
#     iter = 0
#     # r = [None for i in range(len(x0))]
#     x1 = [None for i in range(len(x0))]
#     #step 2
#     while(error > tol and iter < maxIter):
#         # the next to for loops are to represent step 3.  
#         for i in range(n):
#             sum =0
#             for j in range(n):
#                 if j != i:
#                     sum += -1 * A[i][j]  * x0[j] + b[i]
#             x1[i] = sum / A[i][i]
#         #step 4
#         error = l2NormErr(b, matrixVectMult(A, x1))
#         if error < tol:
#             return x1
#         #step 5
#         iter += 1
#         #step 6
#         for i in range(n):
#             x0[i] = x1[i]
#         print(x0)       

#     if iter ==  maxIter:
#         print("no solution reached", x1)
#         return "Maxiterations was reached. "
        





def jacobiIteration(A, b, x0, tol, maxIter):
    
    resid = vecSub(b, matrixVecMult(A, x0))

    print(resid)
    for i in range(maxIter):
        print(resid)
        print("l2 norm of resid", l2Norm(resid))
        if l2Norm(resid) < tol:
            return x0
        DinvResid = [] # D inverse * R _k
        for i in range(len(resid)):
            DinvResid.append( ( 1 / A[i][i] ) * resid[i] )
        x0 = vecAdd(x0, DinvResid)
        resid = vecSub(b, matrixVecMult(A, x0))
    
    if iter ==  maxIter:
        print("no solution reached", x0)
        print(x0)
        return "Maxiterations was reached. "






def main():
    A = [ [3, -7, -2, 2],
        [-3, 5, 1, 0],
        [6, -4, 2, -5],
        [-9, 5, -5, 12]]
    # C = [[3, -2, 1],
    #         [1, -3, 2],
    #         [-1, 2, 4]]

    b = [-5, 5, -15, 35]
  
    print("A = ", A)
    print("b = ", b)
    x0 = [1 for j in range(len(b))]
    tol = .1
    maxiter = 3
    x = jacobiIteration(A, b, x0, tol, maxiter)
    print("The solution of Ax = b")
    print(x)


main()
