

**Routine Name:**           newtonRoot

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will calculate the root of a function using the newton's root finding method. It tends
to be better than bisection. 

**Input:** There are multiple inputs needed for this function. It requires the function, it's derivative, x0, the maximum number of 
iterations, and the error. 

**Output:** There two possible results. It will either return the root, or nothing. In the case that it returns nothing
it will print that the max number of iterations was reached. 

**Usage/Example:**

Here is an example of the results. We passed in the parameters that were passed in.
Iterations should be an integer.  

Funciton with starting x = 0.7 with an error of 0.001 and a max number of iterations of 80
root = secantRoot(func, df, x0, maxIter, error)
print("Root: ", root)
Root:  0.8053798589833953



**Implementation/Code:** The following is the code for smaceps()

            
      import math
      
      def newtonRoot(func, df, x0, maxIter, err):
          if abs(func(x0)) < err: 
              return x0
          xNext = x0
          for i in range(maxIter):
              if df(x0) == 0:
                  return "Mathematical error"
              xNext = x0 - func(x0)/df(x0)
              if abs(xNext - x0) < err:
                  return xNext
              x0 = xNext
      
          print("Max iterations reached. ")
            
**Last Modified:** Oct/2021
