# Task 6
# https://habr.com/ru/post/349860/#Zadachi__1


import re


text = """Это курс информатики соответствует ФГОС и ПООП, 
это подтверждено ФГУ ФНЦ НИИСИ РАН"""


def main(text_):
    for match in re.finditer(r'(?:[А-Я]){2,}(?: (?:[А-Я]){2,})*', text_, flags=re.MULTILINE):
        print(match[0] if match else '')


if __name__ == '__main__':
    main(text)
