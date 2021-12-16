#Math 4610 Fundamentals of Computational Mathematics Software Manual Template File


**Routine Name:**           vecOps: vecAdd, vecSub, dotProd, outerProd

**Author:** Riley May

**Language:** python

**Description/Purpose:** This program calculates various vector operations. Those are vector addition (vecAdd), vector subtraction (vecSub),dot product (dotProd), and outer product (outerProd).

**Input:** The input for this program is two differente vectors. In the case of the dot product and outer product they need 
to be vectors of the same size. 

It is important to note that the vector that in vector subtraction that
that it goes first vector minus the second. 
In outer product: it the first vector times the second vector transposed

**Output:** 
For vector addition and subtraction it outputs a list (vector).  
For dot product it will be an integer.    
For outer productit will be a two dimensional list. 

**Usage/Example:**

These are basic vector operations

    x = [1, 2, 3]
    y =  [4, 5, 6, 7]
    z =  [2, 3, 1]
    x + y =  [5, 7, 9, 7]
    x - y = [-4, -5, -6, -7]
    dot product of x, z = 11
    Outerproduct x * z = [[2, 3, 1], [4, 6, 2], [6, 9, 3]]

**Implementation/Code:** The following is the code for vecOps


      def vecAdd(x, y):
          #adds to vectors together
          if len(x) > len(y):
              for i in range(len(y)):
                  x[i] += y[i]
              return x
          else:
              for i in range(len(x)):
                  y[i] += x[i]
              return y

      def vecSub(x, y):
          #code for the the second vector subtracted from the first
          if len(x) >= len(y):
              for i in range(len(y)):
                  x[i] -= y[i]
              return x
          else:
              new = [None] *  len(y) 
              for i in range(len(x)):
                  new[i] = x[i] - y[i]
              for j in range(len(x), len(y)):
                  new[j] = y[j] * -1
              return new

      def dotProd(x, y):
          #This code returns the dot product if the vectors are of the same size
          if len(x) != len(y):
              return "Vectors are not in the same R"
          else:
              prod = 0
              for i in range(len(x)):
                  prod += x[i] * y[i]
              return prod

      def outerProd(x, y):
          #the is code calculates an outer product
          if len(x) != len(y):
              return "Vectors are not in the same R"
          #This initializes it to be the size that we want. 
          result = [[None for i in range(len(y))] for k in range(len(x))]
          for j in range(len(y)):
              for k in range(len(x)):
                  result[k][j] = y[j] * x[k]
          return result

**Last Modified:** December/2021
