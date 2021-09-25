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
        print(i, error)

def main():
    singlePrecision()


main()
