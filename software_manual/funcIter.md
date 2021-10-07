

**Routine Name:**           funcIter

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will compute a single root based off the input given to it. It take 4 parameters. 
It requires that the function converges. 

The program ends whent the tolerane/ error is met, or the max number of iterations threshold is reached. 

**Input:** There are 4 inputs needed. 1 is the  starting point or x_0. It is where the function starts iterating from.
2 the function. 
3  The tolerance.
4 The max number of iterations. 

If only the first 3 are inputted it will default to 50 iterations. If only the first 2 are inputted it should default to a tolerance 
of .1  and max iterations of 100. These aren't ideal, but good for testing your first two inputs. 

**Output:** This routine returns a string saying if a route was found, what it was, and the number of iterations when the program ended. 


**Usage/Example:**

This routine is used to find the roots of a function. It isn't the best way to find the root of an equation. 
It can find routes, but it is not the most efficient. 

It returns strings stating what happened. 

**Implementation/Code:** The following is the code for funcIter()


      c # fx is funciton of x, tol is for the tolerance,  maxIter is max iterations
      c def fixedPoint(x0, fx, tol =.1 , maxIter = 100):
      c     iter = 0
      c     error = 10 * tol
      c     while(error > tol and iter < maxIter):
      c         x1 = x0 - fx(x0)  #g(x) is defined to be x - f(x)
      c         error = abs(x1 - x0)
      c         x0 = x1
      c         iter += 1
      c         #print(iter)
      c     if iter == maxIter:
      c         return "No root found in " + str(iter) +  " iterations. The was the last value: " + str(x0)
      c     else:
      c         return str(x0) +  " at  " + str(iter) + "  iterations."

**Last Modified:** Oct/2021
