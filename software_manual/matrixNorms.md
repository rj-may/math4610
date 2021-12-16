#Math 4610 Fundamentals of Computational Mathematics Software Manual Template File
This is a template file for building an entry in the student software manual project. You should use the formatting below to
define an entry in your software manual.

**Routine Name:**           matrixNorms.py

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will compute an L1, L2, or L infinity norm for a matrix depending on what function is called. 


**Input:** The only input is 1 SQUARE matrix of real values. 

**Output:** This routine returns a single value. 

**Usage/Example:**

This creates matrix norms for SQUARE matrices. It only needs to take a matrix an example. On the digaonlly dominant square matrix of size 100 (that code is also documented). 

      L1 Norm: 797, 797, 766, 765, 765
      L2 Norm: 208.269056751117, 204.71199280941016, 210.24271687742242, 207.95432190748045, 205.68908575809266
      L Infninty Norm: 199, 198, 200

**Implementation/Code:** The following is the code for matrixNorms()

      import sys
      sys.path.insert(0, '../lib/')

      from matrix.vecNorms import l1Norm
      from matrix.vecNorms import l2Norm
      from matrix.vecNorms import lInfNorm


      def l1MatrixNorm(matrix):
          size = len(matrix)
          norm = 0
          for i in range(size):
              testList = [None for j in range(size)]
              for j in range(size):
                  testList[j] = matrix[i][j]
              testNorm = l1Norm(testList)
              if testNorm > norm:
                  norm = testNorm
          return norm

      def l2MatrixNorm(matrix):
          size = len(matrix)
          norm = 0
          for i in range(size):
              testList = [None for j in range(size)]
              for j in range(size):
                  testList[j] = matrix[i][j]
              testNorm = l2Norm(testList)
              if testNorm > norm:
                  norm = testNorm
          return norm


      def lInfMatrixNorm(matrix):
          size = len(matrix)
          norm = 0
          for i in range(size):
              testList = [None for j in range(size)]
              for j in range(size):
                  testList[j] = matrix[i][j]
              testNorm = lInfNorm(testList)
              if testNorm > norm:
                  norm = testNorm
          return norm


**Last Modified:** December/2021
