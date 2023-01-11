# put your python code here
n, m1 = map(int, input().split())
mx_1 = []
for _ in range(n):
    tmp1 = list(map(int, input().split()))
    mx_1.append(tmp1)

input()

m2, k = map(int, input().split())
mx_2 = []
for _ in range(m2):
    tmp2 = list(map(int, input().split()))
    mx_2.append(tmp2)

mult_mx = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        s = 0
        for x in range(m1):
            s += mx_1[i][x] * mx_2[x][j]
        mult_mx[i][j] = s

for row in mult_mx:
    print(*row)