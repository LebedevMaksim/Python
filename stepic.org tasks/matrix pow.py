def matrix_pow(matrix_, p):
    n, m = len(matrix_), len(matrix_[0])
    if p < 0 or n != m:
        result = False
    elif p == 0:
        result = [[0]*m for _ in range(n)]
    elif p == 1:
        result = matrix_.copy()
    else:
        result = [[0]*m for _ in range(n)]
        for i in range(n):
            result[i] = matrix_[i].copy()

        for _ in range(2, p + 1):
            for j in range(n):
                for i in range(n):

                    s = 0
                    for k in range(n):
                        s += result[i][k] * matrix_[k][j]

                    result[i][j] = s

    return result


def matrix_print(matrix_):
    for row in matrix_:
        for item in row:
            print(str(item).ljust(4), end='')
        print()


matrix = [
    [1, 0],
    [4, 1],
]

res = matrix_pow(matrix, 25)

matrix_print(res)
