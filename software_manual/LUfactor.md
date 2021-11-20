#Math 4610 Fundamentals of Computational Mathematics Software Manual file

**Routine Name:**           Lufactor

**Author:** Riley May

**Language:** python

**Description/Purpose:** This code is to compute the LU factorization of a matrix. It is assuming good pivots in the elimination steps. 
It will out two matrices L and U such L * U = A. It should work on most square independent matrices. 
This is good for solving different values of b instead of recombuting an elimiated b every time. 


**Input:**  It take two dimensional list (matrix) as the input 

**Output:** It outputs two two-dimensional lists (2 matrices) as the output. 

**Usage/Example:** 

This code can factor the matrices out. This is good for solving different values of b instead of recombuting an elimiated b every time. 

Original matrix    
[3, -7, -2, 2]    
[-3, 5, 1, 0]     
[6, -4, 0, -5]    
[-9, 5, -5, 12]   
Lower =     
[1, 0, 0, 0]      
[-1.0, 1, 0, 0]   
[2.0, -5.0, 1, 0]       
[-3.0, 8.0, 3.0, 1]     
Upper =     
[3, -7, -2, 2]    
[0.0, -2.0, -1.0, 2.0]        
[0.0, 0.0, -1.0, 1.0]   
[0.0, 0.0, 0.0, -1.0]   

**Implementation/Code:** The following is the code for LUfactor()

      ## LU factorization for square matrix
      def LUfactor(mtrx):
          n = len(mtrx)
          lower = [[0 for i in range(n)] for i in range(n)]
          for i in range(n):
              lower[i][i] = 1
          for k in range(0, n-1):
              for i in range(k+1, n):
                  factor = mtrx[i][k] / mtrx[k][k]
                  for j in range(k, n):
                      mtrx[i][j] -= (factor * mtrx[k][j]) 
                  lower[i][k] = factor
                  
          return lower, mtrx
          
**Last Modified:** November/2021
