
#This code performs various vector opertations. 

def vecAdd(x, y):
    #adds to vectors together
    if len(x) > len(y):
        for i in range(len(y)):
            x[i] += y[i]
        return x
    else:
        for i in range(len(x)):
            y[i] += x[i]
        return y

def vecSub(x, y):
    #code for the the second vector subtracted from the first
    if len(x) >= len(y):
        new = [None for i in range(len(x))]
        for i in range(len(y)):
            new[i] = x[i]  - y[i]
        return new
    else:
        new = [None] *  len(y) 
        for i in range(len(x)):
            new[i] = x[i] - y[i]
        for j in range(len(x), len(y)):
            new[j] = y[j] * -1
        return new

def dotProd(x, y):
    #This code returns the dot product if the vectors are of the same size
    if len(x) != len(y):
        return "Vectors are not in the same R"
    else:
        prod = 0
        for i in range(len(x)):
            prod += x[i] * y[i]
        return prod

def outerProd(x, y):
    #the is code calculates an outer product
    if len(x) != len(y):
        return "Vectors are not in the same R"
    #This initializes it to be the size that we want. 
    result = [[None for i in range(len(y))] for k in range(len(x))]
    for j in range(len(y)):
        for k in range(len(x)):
            result[k][j] = y[j] * x[k]
    return result

def main():
    x = [1, 2, 3]
    print("x =", x)
    y = [4, 5, 6, 7]
    print("y = ", y)
    z = [2, 3, 1]
    print("z = ", z)
    r1 = vecAdd(x, y)
    print("x + y = ", r1)
    r2 = vecSub(x, y)
    print("x - y =",  r2)
    r3 = dotProd(x, z)
    print("dot product of x, z =", r3)
    r4 = outerProd(x, z)
    print("Outerproduct x * z =", r4)

main()
