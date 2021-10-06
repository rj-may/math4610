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

      c from matplotlib import pyplot as plt
      c import numpy as np
      c #
      c 
      c def graphFunc(*args):
      c     for arg in args:
      c         xVal = []
      c         yVal = []
      c         for i in range(-20, 21):
      c             xVal.append(i)
      c             eq = arg.replace("x", str(i))
      c             y = eval(eq)
      c             yVal.append(y)
      c         plt.plot(xVal, yVal, label = arg)
      c     plt.legend()
      c     plt.xlabel("X axis")
      c     plt.ylabel("Y axis")
      c     plt.show()
      c 
      c 
**Last Modified:** Oct 2021
