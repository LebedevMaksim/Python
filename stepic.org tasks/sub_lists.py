"""Извлекает все возможные подстроки из заданной строки (задача на **)"""


def sub_lists(li):
    res = [[]]
    ln = len(li)
    for i in range(ln, -1, -1):
        for j in range(i):
            tmp = []
            for k in range(ln - i + 1):
                s = li[k + j]
                tmp.append(s)
            res.append(tmp)
    return res


inp = list('a b c d'.split())

print(sub_lists(inp))
