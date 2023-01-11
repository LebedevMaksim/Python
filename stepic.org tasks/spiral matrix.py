# put your python code here
n, m = map(int, input().split())
matr = [[0] * m for _ in range(n)]
i, j = 0, 0
di, dj = 0, 1

for x in range(1, n * m + 1):
    matr[i][j] = x
    if dj == 1 and (j + 1 == m or matr[i][j + 1]):
        di, dj = 1, 0
    if di == 1 and (i + 1 == n or matr[i + 1][j]):
        di, dj = 0, -1
    if dj == -1 and (j - 1 < 0 or matr[i][j - 1]):
        di, dj = -1, 0
    if di == -1 and matr[i - 1][j]:
        di, dj = 0, 1

    i += di
    j += dj

for row in matr:
    for item in row:
        print(str(item).ljust(3), end='')
    print()
