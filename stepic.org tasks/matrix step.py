# put your python code here
n, m = map(int, input().split())
matr = [[i + 1 for i in range(m)] for _ in range(n)]

for i in range(1, n):
    for j in range(m):
        matr[i][j] = matr[i - 1][j - m + 1]

for row in matr:
    for item in row:
        print(str(item).ljust(3), end='')
    print()
