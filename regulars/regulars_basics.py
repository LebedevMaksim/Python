import re


match = re.search(r'\d\d\D\d\d', r'Number 123-45-45')
print(match[0] if match else '<not found>')

match = re.fullmatch(r'\d\d\D\d\d', r'64-64')
print("Match" if match else 'NO')

print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'))

string_data = r'Ищет группу цифр, похожую на дату. И 15.01.2000 и 99.88.5555 найдет!'

print(re.findall(r'\d\d.\d\d.\d{4}', string_data))

for m in re.finditer(r'\d\d.\d\d.\d{4}', string_data):
    print(f'Дата {m[0]} начинается с позиции {m.start()}')

print(re.sub(r'\d\d.\d\d.\d{4}', r'DD.MM.YYYY', string_data))

# flags=re.ASCII
print(re.findall(r'\w+', 'Hello, мир!', flags=re.ASCII))

# flags=re.IGNORECASE
print(re.findall(r'[уяыаоэию]+', 'ООО ааа ыыы ффф ЯЯЯ иии ТТТ', flags=re.IGNORECASE))

# flags=re.MULTILINE
text = r"""
Текст со строками и переносами
строка2
строка3 и конец
"""

print(re.findall(r'^стр\w+', text, flags=re.MULTILINE))
