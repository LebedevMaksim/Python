import copy


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

        for _ in range(p - 1):
            res = [[0]*n for _ in range(n)]
            for j in range(n):
                for i in range(n):

                    s = 0
                    for k in range(n):
                        s += result[i][k] * matrix_[k][j]

                    res[i][j] = s
            result = copy.deepcopy(res)

    return result


def matrix_print(matrix_):
    for row in matrix_:
        for item in row:
            print(str(item).ljust(10), end='')
        print()


def matrix_input(n):
    matrix_ = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        matrix_.append(tmp)

    return matrix_


def main():
    n = int(input())
    matrix = matrix_input(n)

    p = int(input())
    res = matrix_pow(matrix, p)

    matrix_print(res)


if __name__ == '__main__':
    main()
