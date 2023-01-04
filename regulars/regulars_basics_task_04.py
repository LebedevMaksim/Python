# Task 4
# https://habr.com/ru/post/349860/#Zadachi__1


import re


text = """Уважаемые! Если вы к 09:00 не вернёте 
чемодан, то уже в 09:00:01 я за себя не отвечаю. 
PS. С отношением 25:50 всё нормально!"""


def main(text_):
    print(re.sub(r'(?:(?:[0-1][0-9])|(?:2[0-4]))(?::[0-5][0-9]){,2}', 'TBD', text_))


if __name__ == '__main__':
    main(text)
