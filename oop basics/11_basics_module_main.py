# author: MLebedev
""" Практика по ООП #11

https://younglinux.info/oopython/module

В практической работе урока 7 "Композиция" требовалось разработать интерфейс
взаимодействия с пользователем. Разнесите сам класс и интерфейс по разным файлам.
Какой из них выполняет роль модуля, а какой – скрипта?
Оба файла можно поместить в один каталог

"""


import math
from room import Room


def main():
    x, y, h = map(float, input('Please enter the width, length and height, \nseparated by space:').split(sep=' '))
    r1 = Room(x, y, h)
    print('Room square:', r1.square)

    wd_i = int(input('How many windows and doors there are in the room:'))
    for i in range(wd_i):
        a, b = map(float, input('Please enter the width and height, \nseparated by space:').split(sep=' '))
        r1.add_wd(a, b)

    work_s = r1.work_surface()
    print('Work surface:', work_s)

    r_w, r_h = map(float, input('Please enter the wallpaper width and height, \nseparated by space:').split(sep=' '))
    r_count = math.ceil(work_s / (r_w * r_h))
    print('Wallpaper rolls count:', r_count)


if __name__ == '__main__':
    main()
