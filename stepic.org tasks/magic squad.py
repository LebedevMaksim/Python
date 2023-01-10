# put your python code here
n = int(input())
squad = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    squad.append(tmp)

flag = True
sm = sum(squad[0])

for i in range(1, n):
    if sum(squad[i]) != sm:
        flag = False

if flag:
    for j in range(n):
        sum_col = 0
        for i in range(n):
            sum_col += squad[i][j]
        if sum_col != sm:
            flag = False

if flag:
    sum_a, sum_b = 0, 0
    for i in range(n):
        sum_a += squad[i][i]
        sum_b += squad[i][n - i - 1]
    if sum_a != sm or sum_b != sm:
        flag = False

if flag:
    nums = []
    for line in squad:
        nums.extend(line)

    for x, n in enumerate(sorted(nums)):
        if x + 1 != n:
            flag = False

print('YES' if flag else 'NO')
