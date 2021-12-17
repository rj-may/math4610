#Math 4610 Fundamentals of Computational Mathematics Software Manual


**Routine Name:**           powerMethod

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will caclulate the largest eigen value of a matrix via the  power method. 

**Input:** The inputs for the program are a matrix, an initial eigen vector guess, initial eigen vector, tolerance, and maxiterations. 

**Output:** This routine returns a single numerical eigenvaulue. It should be the largest eigen value of a matrix. 
**Usage/Example:**

This routinw outputs the largest eigenvalue usign the power method. 

When I ran this code on 100x100 matrix diagonally dominant matrix , it produced the following eigeenvalues.           
    largest eigen value =  228.05502704975788              
    largest eigen value =  214.79032495455218                                  
    largest eigen value =  220.32854192962827                                

**Implementation/Code:** The following is the code for powerMethod()

    def powerMethod(matrix, x0, lmbd0, tol, maxiter): #lmbd0 refers to initial guess of the eigen value
        error  = tol +1
        for i in range(maxiter):
            y = matrixVecMult(matrix, x0)
            ## normal y
            euclid = l2Norm(y)
            for i in range(len(y)):
                y[i] = y[i]/ euclid
            v = y
            lmbd1 = dotProd(v, matrixVecMult(matrix, v))
            # print("lmd1 = ", lmbd1)
            error = abs(lmbd1 - lmbd0)
            lmbd0 = lmbd1
            x0 = v
            if error < tol:
                return lmbd0
        else:
            print("Max iterations were reached")
            return lmbd0

Date modified Dec/2021
