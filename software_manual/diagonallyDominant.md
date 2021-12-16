#Math 4610 Fundamentals of Computational Mathematics Software Manual


**Routine Name:**           diagDom.py

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine outputs the a 100 by 100 matrix that is diagonally dominant. It is good for testing things
such as matrix norms and power methods for finding eigen values. 


**Input:** The are no inputs. 

**Output:** This routine returns a 100 x 100 diagonally domominant matrix that has diagonal values between 101 and 200, and
the other values are between -10 and 10. 

**Usage/Example:**

This routine outputs the a 100 by 100 matrix that is diagonally dominant.   
    The output of the code is too large to demonstrate in this file. 
    

**Implementation/Code:** The following is the code for diagonallyDominant()

    from random import randint

    def diagonallyDominant():
       matrix = [[None for i in range(100)] for j in range(100)]
       for i in range(100):
           for j in range(100):
               if i == j:
                   matrix[i][j] = randint(101, 200)
               else:
                   matrix[i][j] = randint(-10, 10)
       return matrix

Date modified Dec/2021
