# Task 7
# https://habr.com/ru/post/349860/#Zadachi__1


import re


text = """Было закуплено 12 единиц техники 
по 410.37 рублей."""


def cube_match(match):
    return str(int(match[0]) ** 3)


def main(text_):
    coded = re.sub(r'\d+', cube_match, text_, flags=re.MULTILINE)
    print(coded)


if __name__ == '__main__':
    main(text)
