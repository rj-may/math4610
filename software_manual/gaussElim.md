#Math 4610 Fundamentals of Computational Mathematics Software Manual 

**Routine Name:**           gaussElim 

**Author:** Riley May

**Language:** python

**Description/Purpose:** This method is to reduce a linear system of equations. It performs Guassian elimination,
so that way backsolved. This should work on a independent square system. 

**Input:** This method takes a square matrix (two dimensional list), and a vector (list). 

**Output:** This method returns a matrix and vector after having performed Gaussian elimination. 
**Usage/Example:**

This method takes a matrix (two dimensional list), and a vector (list). It performs Gaussian elimination on them. 

Here is an example of the output.       
      Original matrix    
      [8, 1, -2, -3]  
      [-1, -10, 2, 5]      
      [1, -6, 12, -3]    
      [-3, 2, 3, -9]     
      Eliminated matrix  
      [8, 1, -2, -3]        
      [0.0, -9.875, 1.75, 4.625]    
      [0.0, 0.0, 11.164556962025316, -5.493670886075949]  
      [0.0, 0.0, 0.0, -7.698412698412699]             
      Eliminated col 1s                      
      [1, 1.125, 0.17721518987341778, 1.603174603174603]  
      

**Implementation/Code:** The following is the code for smaceps()
      
       def gaussElim(mtrx, vecB):
          n = len(vecB)
          for k in range(0, n-1):
              for i in range(k+1, n):
                  factor = mtrx[i][k] / mtrx[k][k]
                  for j in range(k, n):
                      mtrx[i][j] -= (factor * mtrx[k][j]) 
                  vecB[i] -= factor * vecB[k]
          
          return mtrx, vecB

**Last Modified:** Nov/2021
