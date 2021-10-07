

**Routine Name:**           bisection

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will compute a single root based off the input given to it. It take 4 parameters. 
It requires that f(a) and f(b) are different signs +/-.

The program ends when the number of iterations threshold is reached.  The number of iteration is based off the error and difference
between a and b. 

**Input:** There are 4 inputs needed. 
1 is the  starting point "a"
2 the end point "b" 
3  The function   
4 The tolerance. 


**Output:** This routine returns a string saying no route was found, or the root of a float. 


**Usage/Example:**

This routine is used to find the roots of a function. It isn't the best way to find the root of an equation. 
It can find routes, but it is not the most efficient. 

It returns strings stating what happened. 

**Implementation/Code:** The following is the code for bisection()

      c  
      c  #Tasksheet 4 Task 5
      c  from math import log2
      c  from math import ceil
      c  import math # this is for any functions that we pass into it. 
      c  
      c  
      c  def bisection(a, b, func, tol):
      c      fa = func(a)
      c      fb = func(b)
      c      if (fa * fb > 0): return "No root in [a,b] or f(a) and f(b) have the sign."
      c      e0 = abs(b -a) #initial error
      c      k = ceil(log2(e0/tol)) #This is the number of iterations we will do. Round up to ensure it works. 
      c  
      c      for i in range(k):
      c          c = .5 * (a + b)
      c          fc = func(c)
      c          if (fa * fc < 0):
      c              b =c 
      c              fb = fc
      c          else:
      c              a = c
      c              fa = fc
      c  
      c      return c 
      c      
      c     
      
      
**Last Modified:** Oct/2021
