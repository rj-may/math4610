
import sys
sys.path.insert(0, '../lib/')

from matrix.geScaledPivot import  geScaledPivot
from matrix.backsolve import backsolve


def hilbertMatrix(size):
    hilbert = [[None for i in range(size)] for k in range(size)]
    for i in range(size):
        for k in range(size):
            hilbert[i][k] = 1 / ( (i+1) + (k+1)  -1)

    b =[1 for k in range(size)]
    return hilbert, b


def main():
    for i in range (4, 11):
        print("Solving for Hilbert matrix size: ", i)
        A, b, = hilbertMatrix(i)
        A, b = geScaledPivot(A, b)
        x = backsolve(A, b)
        for i in range(len(x)):
            x[i] = round(x[i],6)
        print(x)


main()
