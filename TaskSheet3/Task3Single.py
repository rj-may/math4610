#Single precision of of machine epislon
import numpy as np

def singlePrecision():
    x = 1
    eps = (1/2) #epsilon
    for i in range(40):
        xApprox = x + eps
        error = abs(x - xApprox)
        if error == 0:
            break
        eps = np.finfo(np.single).eps
        print(i, error)

def main():
    singlePrecision()


main()
