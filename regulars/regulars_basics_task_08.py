# Task 8
# https://habr.com/ru/post/349860/#Zadachi__1


import re


text_a = """Московский государственный институт международных отношений"""

text_b = """микоян авиацию снабдил алкоголем, 
народ доволен работой авиаконструктора"""


def main(text_):
    res = re.findall(r'(\w)(?:\w+)', text_, flags=re.MULTILINE)
    print(''.join(res).upper())


if __name__ == '__main__':
    main(text_a)
    main(text_b)
