# put your python code here
n, m = map(int, input().split())
matr = [[0]*m for _ in range(n)]
x = 1

for j in range(m):
    for k in range(n):
        if k < n and j - k > -1:
            matr[k][j - k] = x
            x += 1

# i = 1, j = m - 1
for i in range(1, n):
    for j in range(m):
        if i + j < n:
            matr[i + j][m - j - 1] = x
            x += 1


for row in matr:
    for item in row:
        print(str(item).ljust(3), end='')
    print()
