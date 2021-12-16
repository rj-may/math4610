#Math 4610 Fundamentals of Computational Mathematics Software Manual


**Routine Name:**           powerMethodInverse.py

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will caclulate the smallest eigenvalue of a matrix via the  inverse power method. 

**Input:** The inputs for the program are a matrix, an initial eigen vector guess, initial eigen vector, tolerance, and maxiterations. 

**Output:** This routine returns a single numerical eigenvaulue. It should be the smallest eigen value of a matrix. 

**Usage/Example:**

This rout outputs the smallest eigenvalue using the inverse power method. 

When I ran this code on 100x100 matrix diagonally dominant matrix , it produced the following eigenvalues.
These are the output results from TaskSheet 10 task 2

smallest eigen value =  0.008942053185438177   
smallest eigen value =  0.009319038875442049                                     
smallest eigen value =  0.009428293243981235                                

**Implementation/Code:** The following is the code for powerMethodInverse()

    def powerMethodIinverse(matrix, x0, lmbd0, tol, maxiter): #lmbd0 refers to initial guess of the eigen value
        error  = tol +1
        for i in range(maxiter):
            y = LUsolver(matrix, x0)  # y = "A ^ -1  * x0"
            ## normal y
            euclid = l2Norm(y)
            for i in range(len(y)):
                y[i] = y[i]/ euclid
            v = y # v = y normalized
            q = LUsolver(matrix, v)         # this is the calcultion of matrix inverse times v.   OR "A -1" * v by solvign Aq = v
            lmbd1 = dotProd(v, q) # dotting v  and q    
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
