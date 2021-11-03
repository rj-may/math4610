# here is the double precision  part of the project
# This is to test the double precision part of the project
import numpy as np

def doublePrecision():
    print("Iteration, machine epsilon")
    x = np.float64(1)
    eps = np.float64(1/2) #epsilon
    for i in range(100):
        xApprox = x + eps
        error = abs(x - xApprox)
        if error == 0:
            break
        eps = np.float64(eps /2)
        print(i, error)

doublePrecision()
