#Math 4610 Fundamentals of Computational Mathematics Software Manual Template File
This is a template file for building an entry in the student software manual project. You should use the formatting below to
define an entry in your software manual.

**Routine Name:**           doubleMachEps

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will compute the double precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case. Even though there are arguments supplied, the real purpose is to
return values in those variables.

**Output:** This routine returns a doulbe precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**
This code has little usage. it is the default for python number unless specifiec otherwise. It does provide a good example of how to use the package numby to create the results wanted with your code.

**Implementation/Code:** The following is the code for doublePrecision().

# here is the double precision  part of the project
# This is to test the double precision part of the project
import numpy as np

    c def doublePrecision():
    c     print("Iteration, machine epsilon")
    c     x = 1
    c     eps = 1/2 #epsilon
    c     for i in range(100):
    c         xApprox = x + eps
    c         error = abs(x - xApprox)
    c         if error == 0:
    c             break
    c         eps = np.float64(eps /2)
    c         print(i, error)
    c 
