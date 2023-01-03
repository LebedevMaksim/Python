# Task 01
"""
У частных легковых автомобилей номера — это буква, три цифры, две буквы,
затем две или три цифры с кодом региона.
У такси — две буквы, три цифры, затем две или три цифры с кодом региона.
"""


import re


nums = [
    'С227НА777',
    'КУ22777',
    'Т22В7477',
    'М227К19У9',
    ' С227НА777',
]


def main():
    for num in nums:
        if re.fullmatch(r'\w\d{3}\w\w\d{2,3}', num):
            print(f'{num} is Private')
        elif re.fullmatch(r'\w\w\d{5,6}', num):
            print(f'{num} is Taxi')
        else:
            print(f'{num} <no match>')


if __name__ == '__main__':
    main()
