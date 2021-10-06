#Math 4610 Fundamentals of Computational Mathematics Software Manual Template File
This is a template file for building an entry in the student software manual project. You should use the formatting below to
define an entry in your software manual.

**Routine Name:**           graph

**Author:** Riley May

**Language:** python

**Description/Purpose:** This program will take multiple strings and graph them. They must be inputted in as strings 
and in code format. Ex: "x ** 2", " 10x - 5"

**Input:** This program takes an infinite number of inputs and graphs. They must be entered in python code format. 
y = x^2 + 5  should be entered as "x **2 +5"
y = sin(x) should be entered as "math.sin(x)"

**Output:** This output a single graph with all the functions on it. 


**Usage/Example:**
Done by example
from graphy.py import graphFunc as g

g(".5 * (x -5) **2 + 3", "5- 10x")


**Implementation/Code:** The following is the code for smaceps()

      subroutine smaceps(seps, ipow)
    c
    c set up storage for the algorithm
    c --------------------------------
    c
          real seps, one, appone
    c
    c initialize variables to compute the machine value near 1.0
    c ----------------------------------------------------------
    c
          one = 1.0
          seps = 1.0
          appone = one + seps
    c
    c loop, dividing by 2 each time to determine when the difference between one and
    c the approximation is zero in single precision
    c --------------------------------------------- 
    c
          ipow = 0
          do 1 i=1,1000
             ipow = ipow + 1
    c
    c update the perturbation and compute the approximation to one
    c ------------------------------------------------------------
    c
            seps = seps / 2
            appone = one + seps
    c
    c do the comparison and if small enough, break out of the loop and return
    c control to the calling code
    c ---------------------------
    c
            if(abs(appone-one) .eq. 0.0) return
    c
        1 continue
    c
    c if the code gets to this point, there is a bit of trouble
    c ---------------------------------------------------------
    c
          print *,"The loop limit has been exceeded"
    c
    c done
    c ----
    c
          return
    end

**Last Modified:** September/2017
