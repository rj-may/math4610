import matplotlib.pyplot as plt


#import stuff from Task1 
xVal = 2

def secDerivApprox(x, h):
    approximation = (cos(x + h) - 2 * cos(x) + cos(x - h)) / (h **  2)
    return approximation



def main():
    actual = -cos(xVal)
    hVal = []
    diff = []
    print(format("h", "<6") + format("\t -cos(2)", "<25") + format("Central diff Approx ", "<24") + format("Difference", "<20"))
    for i in range(-1,17):
        if i == -1:
            h = 1
            approx = secDerivApprox(xVal, h)
        elif i == 0:
            h = 0.5
            approx = secDerivApprox(xVal, h)
        else:
            h = 1 * (10 ** (-1 * i))
            approx = secDerivApprox(xVal, h)
        hVal.append(h)

