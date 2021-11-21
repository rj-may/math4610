#Math 4610 Fundamentals of Computational Mathematics Software Manual 

**Routine Name:**           geScaledPivot.py 

**Author:** Riley May

**Language:** python

**Description/Purpose:** This method is to reduce a linear system of equations. It performs Guassian elimination. It does scaled partial pivoting to 
handle issues with row reduction. It first divides all the rows by the entry in the row with the greatest magnitude. Then before using each pivot,
it takes the entry with the largest magnitude from the column to choose the pivot. 


**Input:** This method takes a square matrix (two dimensional list), and a vector (list). 

**Output:** This method returns a matrix (2 dimensional list) and vector  (list) after having performed Gaussian elimination with scaled pivoting. 



**Usage/Example:**

This method takes a matrix (two dimensional list), and a vector (list). It performs Gaussian elimination on them with scaled pivoting. . 

Here is an example of how it works. It only returns the matrix and the vector, It doesn't show all the intermediate work. 


      
      Original matrix
      [1, -6, 12, -3]   
      [-3, 2, 3, -9]   
      [8, 1, -2, -3]  
      [-1, -10, 2, 5]   
      Scaled matrix   
      [0.08333333333333333, -0.5, 1.0, -0.25]   
      [0.3333333333333333, -0.2222222222222222, -0.3333333333333333, 1.0]  
      [1.0, 0.125, -0.25, -0.375]   
      [0.1, 1.0, -0.2, -0.5]   
      We swapped rows the following rows 0 and 2  
      We swapped rows the following rows 1 and 3  
      Eliminated matrix with partial pivoting.  
      [1.0, 0.125, -0.25, -0.375]  
      [0.0, 0.9875, -0.17500000000000002, -0.4625]  
      [0.0, 0.0, 0.930379746835443, -0.45780590717299574]  
      [0.0, 0.0, 0.0, 0.8553791887125222]   
      Eliminated col 1s   
      [0.125, -0.1125, 0.014767932489451477, -0.1781305114638448]   
      

**Implementation/Code:** The following is the code for geScaledPivot. ()
      
      
      def geScaledPivot(mtrx, vecB):
          #first scale it to the value with the largest magnitude. 
          rowNum = 0 # I needed this because I couldn't get to the b vector without it. 
          for row in mtrx:
              scale = abs(row[0])
              for i in row:
                  if abs(i) > abs(scale):
                      scale = i
              for k in range(len(row)):
                  row[k] = row[k] / scale
              vecB[rowNum] = vecB[rowNum] /scale
              rowNum += 1
      
          n = len(vecB)
          for k in range(0, n-1):
              partialPivot(mtrx, vecB, k)
              for i in range(k+1, n):
                  factor = mtrx[i][k] / mtrx[k][k]
                  for j in range(k, n):
                      mtrx[i][j] -= (factor * mtrx[k][j]) 
                  vecB[i] -= factor * vecB[k]
          
          return mtrx, vecB
          
      def partialPivot(A, b, diag):
          n = len(b)
          maxIndex = diag #start with assuming the largest magnitude is at the diagonal
          for i in range(diag + 1, n):
              if abs(A[i][diag]) > abs(A[maxIndex][diag]): 
                  maxIndex =  i
          if maxIndex != diag:
              # we need to do some row swapping
              #This here should work without returning anything becuase python is pass by reference.
              A[diag], A[maxIndex] = A[maxIndex], A[diag]
              b[diag], b[maxIndex] = b[maxIndex], b[diag]


**Last Modified:** Nov/2021
