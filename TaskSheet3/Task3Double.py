# here is the double precision  part of the project
# This is to test the double precision part of the project

def doublePrecision():
    x = 1
    eps = 1/2 #epsilon
    for i in range(100):
        xApprox = x + eps
        error = abs(x - xApprox)
        if error == 0:
            break
        eps = eps /2
        print(i, error)

def main():
    doublePrecision()


main()