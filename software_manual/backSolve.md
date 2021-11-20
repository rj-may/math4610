#Math 4610 Fundamentals of Computational Mathematics Software Manual T

**Routine Name:**           backsolve.py

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will compute the solution of an eliminated system of Ax=b. It is great for solving 
systems of linear equations. 

**Input:** A matrix (2 dimensional list), and a vector (list), such that it is the eliminated Ax=b

**Output:** This routine returns a single precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

This function needs two parameters to work. 
It takes a square matrix of any size with its accompanying vector b. This is for the traditional vector Ax=b. 

It returns a vector (list) x such that is the solution. 

Examples:
Eliminated matrix  
[8, 1, -2, -3]   
[0.0, -9.875, 1.75, 4.625]   
[0.0, 0.0, 11.164556962025316, -5.493670886075949]   
[0.0, 0.0, 0.0, -7.698412698412699]     
Eliminated col 1s         
[1, 1.125, 0.17721518987341778, 1.603174603174603] 


Sol x:  [0.053608247422680416, -0.2268041237113402, -0.08659793814432988, -0.20824742268041235] 


**Implementation/Code:** The following is the code for backsolve()


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

**Last Modified:** Nov 2021
