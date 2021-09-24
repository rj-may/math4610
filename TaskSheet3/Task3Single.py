#Single precision of of machine epislon
import numpy as np

def singlePrecision():
    x = 1
    eps = np.float32(1/2) #epsilon
    for i in range(100):
        xApprox = x + eps
        error = abs(x - xApprox)
        if error == 0:
            break
        eps = np.float32(eps / 2)
        print(i, error)

def main():
    singlePrecision()


main()
