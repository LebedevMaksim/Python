# Task 3
# https://habr.com/ru/post/349860/#Zadachi__1


import re


text_a = """Иван Иванович! 
Нужен ответ на письмо от ivanoff@ivan-chai.ru. 
Не забудьте поставить в копию 
serge'o-lupin@mail.ru- это важно.
"""

text_b = """foo.@ya.ru, foo@.ya.ru"""

text_c = """boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru"""


def main(text):
    words = re.split(r'[ ,\n]+', text, flags=re.MULTILINE)

    for word in words:
        if '@' in word:
            mail = re.search(r'[0-9a-zA-Z][0-9a-zA-Z\'\._+-]{,64}[0-9a-zA-Z]@[0-9a-zA-Z][0-9a-zA-Z\.-]{,255}[0-9a-zA-Z]',
                             word, flags=re.ASCII)

            print(word, ' '*(23 - len(word)), mail[0] if mail else '')


if __name__ == '__main__':
    main(text_a + ' ' + text_b + ' ' + text_c)
