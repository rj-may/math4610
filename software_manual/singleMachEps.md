#Math 4610 Fundamentals of Computational Mathematics Software Manual Template File
This is a template file for building an entry in the student software manual project. You should use the formatting below to
define an entry in your software manual.

**Routine Name:**           singleMachEps

**Author:** Riley May

**Language:** python

**Description/Purpose:** This routine will compute the single precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case. Even though there are arguments supplied, the real purpose is to
return values in those variables.

**Output:** This routine returns a single precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**
This code has little usage. It does provide a good example of single precision, and how you must use numpy to round the number


**Implementation/Code:** The following is the code for singleMachEps()

#Single precision of of machine epislon
'''
important note about using numpy sinlge number; when peforming operations on 2 different things 
you have to make sure both are the value that you want. It will default between the larger bit value
Ex : single * double will result with a double. Had to read documentation. 
'''
import numpy as np

def singlePrecision():
    print("Iteration, machine epsilon")
    x = np.single(1)
    eps = np.single(1/2) #epsilon
    for i in range(40):
        xApprox = x + eps
        error = abs(x - xApprox)
        if error == 0:
            break
        eps = np.single(eps / 2)
        print(i, error)7
