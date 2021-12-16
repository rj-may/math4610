# This is for task 2 of tasksheet 9
# the code for this will solve various norms

def l1Norm(x):
    norm = 0
    for i in range(len(x)):
        norm += abs(x[i])
    return norm


def l2Norm(x):
    normsqd = 0
    for i in range(len(x)):
        normsqd += x[i] * x[i]
    norm = normsqd ** (1/2)
    return norm

def lInfNorm(x):
    norm = 0
    for i in range(len(x)):
        if abs(x[i]) > abs(norm):
            norm = x[i]
    return norm

def subtract(x, y):
    if len(x) != len(y):
        return "error in vector size"
    err = [None for i in range(len(x))]
    for i in range(len(x)):
        err[i] = x[i] - y[i]
    return err

def l1NormErr(x, y):
    e = subtract(x, y)
    return l1Norm(e)

def l2NormErr(x, y):
    e = subtract(x, y)
    return l2Norm(e)

def lInfNormErr(x, y):
    e = subtract(x, y)
    return lInfNorm(e)



def main():
    x = [1, 2, 3]
    print("x =", x)
    y = [4, 5, -6, 7]
    print("y = ", y)
    z = [2, -3, 1]
    print("z = ", z)
    r1 = l1Norm(y)
    print("l1 norm of y= ", r1)
    r2 = l2Norm(x)
    print("l2 norm of x=",  r2)
    r3 = lInfNorm(z)
    print("l infinity norm of z=", r3)
    r4 = l1NormErr(x, z)
    print("L1 Norm error of x, z =", r4)
    r5 = l2NormErr(x, z)
    print("L2 Norm error of x, z =", r5)
    r6 = lInfNormErr(x, z)
    print("L infinity Norm error of x, z =", r6)

main()
