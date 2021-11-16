def initialize(size):
    mtrxA = []
    for i in range(size):
        new = []
        for j in range(size):
            if j >= i:
                num = i + 1 +j +1 -1
                new.append(num)
            if j < i:
                new.append(0)
        mtrxA.append(new)
    # print(mtrxA)
    return mtrxA

def transpose(mtrx):
    # mtrxT = mtrx[:][:]
    mtrxT = [[None for j in range(len(mtrx))] for j in range(len(mtrx))]
    # print(mtrxT)
    size = len(mtrx)
    for i in range(size):
        for j in range(size):
            mtrxT[i][j] = mtrx[j][i]
    print("this is mrtxT", mtrxT)
    # for i in mtrxT:
    #     for j in i:
    #         print(j, end=" ")
    #     print(" ")
    return mtrxT

def main():
    A = initialize(3)
    print(A)
    AT = transpose(A)
    print(AT)

main()
    
