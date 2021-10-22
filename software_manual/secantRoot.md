

**Routine Name:**           secantRoot  

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will calculate the root of a function using the secant method. It is good because
you don't need the deriviative of the funciton. 

**Input:** There are multiple inputs needed for this function. It requires the function, x0, x1, the maximum number of 
iterations, and the error. 

**Output:** There two possible results. It will either return the root, or nothing. In the case that it returns nothing
it will print that the max number of iterations was reached. 

**Usage/Example:**

Here is an example of the results. We passed in the parameters that were passed in.
Iterations should be an integer. 

Funciton with starting x0 = 0.6,  x1 = 0.9, with an error of 0.001 and a max number of iterations of 80
root = secantRoot(func, x0, x1, maxIter, error)
print("Root: ", root)
Root:  0.8053820324948411



**Implementation/Code:** The following is the code for smaceps()

      
      import math
      
      def secantRoot(func, x0, x1, maxIter, err):
          if abs(func(x0)) < err: 
              return x0
          for i in range(maxIter):
              x2 = x1 - func(x1) * (x1 - x0)/ (func(x1)- func(x0))
              if abs(x2 - x1) < err:
                  return x2
              x0, x1 = x1, x2 # reassigning variables. 
      
          print("Max iterations reached. ")
      
**Last Modified:** Oct/2021
