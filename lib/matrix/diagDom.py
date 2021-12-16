from random import randint

def diagonallyDominant():
    matrix = [[None for i in range(100)] for j in range(100)]
    for i in range(100):
        for j in range(100):
            if i == j:
                matrix[i][j] = randint(101, 200)
            else:
                matrix[i][j] = randint(-10, 10)
    return matrix