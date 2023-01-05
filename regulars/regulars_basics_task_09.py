# Task 9
# https://habr.com/ru/post/349860/#Zadachi__1


import re


text = [
    """Вечер за окном. / Еще один день прожит. / Жизнь скоротечна...""",
    """Просто текст""",
    """Как вишня расцвела! / Она с коня согнала / И князя-гордеца.""",
    """На голой ветке / Ворон сидит одиноко… / Осенний вечер!""",
    """Тихо, тихо ползи, / Улитка, по склону Фудзи, / Вверх, до самых высот!""",
    """Жизнь скоротечна… / Думает ли об этом / Маленький мальчик.""",
]


def main(text_):
    sub_line = re.sub(r'[^еЕёЁуУяЯыЫаАоОэЭиИюЮ/]', '', text_)
    lines = re.split(r'/', sub_line)

    if len(lines) != 3:
        return 'Не хайку. Должно быть 3 строки.'

    for line in range(len(lines)):
        step = 5 + 2 * (line % 2)  # 5 7 5
        if len(lines[line]) != step:
            return f"Не хайку. В {line + 1} строке слогов не {step}, а {len(lines[line])}."

    return 'Хайку!'


if __name__ == '__main__':
    for i in text:
        print(i, ' ' * (70 - len(i)), main(i))
