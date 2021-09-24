from math import cos

xVal = 2

def secDerivApprox(x, h):
    approximation = (cos(x + h) - 2 * cos(x) + cos(x - h)) / (h **  2)
    return approximation



def printDifferenceTable(h, actual, approx):
    diff = abs(actual - approx)
    h_sci_not = "{:.1e}".format(h)
    print(str(h_sci_not) + "\t " + str(actual) + "\t" + format(str(approx), "<20") + "\t" + str(diff))
    return diff


def main():
    actual = -cos(xVal)
    hVal = []
    diff = []
    print(format("h", "<6") + format("\t -cos(2)", "<25") + format("Central diff Approx ", "<24") + format("Difference", "<20"))
    for i in range(-1,17):
        if i == -1:
            h = 1
            approx = secDerivApprox(xVal, h)
            diff.append(printDifferenceTable(h, actual, approx))
        elif i == 0:
            h = 0.5
            approx = secDerivApprox(xVal, h)
            diff.append(printDifferenceTable(h, actual, approx))
        else:
            h = 1 * (10 ** (-1 * i))
            approx = secDerivApprox(xVal, h)
            diff.append(printDifferenceTable(h, actual, approx))
        hVal.append(h)


    print("\n" * 4)



    # https://en.wikipedia.org/wiki/Order_of_accuracy
    print("First column is the step in hVal squared")
    print("Second column is the error")
    print("ratio")
    for i in range(len(hVal) -1):
        hDiffSquared = (hVal[i]  - hVal[i+1]) ** 2
        print(format(hDiffSquared, "<15"), "\t" ,  format(diff[i], "<10"), "\t" , hDiffSquared / diff[i])
        


        
        
    

        
main()
