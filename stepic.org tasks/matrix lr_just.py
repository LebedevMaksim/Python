matrix = [
    [277, 1, -3, 90],
    [0, -11, 280, 400],
    [-8, -5, 995, 1],
]

for row in matrix:
    for num in row:
        print(str(num).rjust(6), end='')
    print()

print('---------------------------')

n = 8
m_square = [[0]*n for _ in range(n)]

for i in range(n):
    m_square[i][i] = 'M'
    m_square[i][n - i - 1] = 'X'

for row in m_square:
    for num in row:
        print(str(num).rjust(3), end ='')
    print()
