#this method returns a hilbert matrix of a given size

def hilbertMatrix(size):
    hilbert = [[None for i in range(size)] for k in range(size)]
    for i in range(size):
        for k in range(size):
            hilbert[i][k] = 1 / ( (i+1) + (k+1)  -1)

    return hilbert
