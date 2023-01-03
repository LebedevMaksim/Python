# Task 2
"""
Слово — это последовательность из букв (русских или английских), внутри которой могут быть дефисы.
На вход даётся текст, посчитайте, сколько в нём слов.
"""


import re


text = r"""Он --- серо-буро-малиновая редиска!! 
>>>:-> 
А не кот. 
www.kot.ru
"""


def main():
    words = re.findall(r'\w[-\w]*', text, flags=re.MULTILINE)
    print(len(words), words)


if __name__ == '__main__':
    main()
