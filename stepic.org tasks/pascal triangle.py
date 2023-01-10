def pascal(n):
    if n == 0:
        res = [1]
    elif n == 1:
        res = [1, 1]
    else:
        res = [1, 1]
        for _ in range(n - 1):
            r = [1]
            for i in range(len(res) - 1):
                r.append(res[i] + res[i + 1])
            r.append(1)
            res = r.copy()
    return res


num = int(input())

for i in range(num):
    print(' ' * (num - i) * 2, pascal(i))  # FIXME - output spaces
