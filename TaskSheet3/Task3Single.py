#Single precision of of machine epislon
import numpy as np

def doublePrecision():
    x = 1
    eps = 1/2 #epsilon
    for i in range(100):
        xApprox = x + eps
        error = abs(x - xApprox)
        if error == 0:
            break
        eps = eps / 2
        eps = np.float32(eps)
        print(i, error)

def main():
    doublePrecision()


main()
