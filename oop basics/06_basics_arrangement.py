# author: MLebedev
""" Практика по ООП #6

https://younglinux.info/oopython/arrangement

Приведенная выше программа имеет ряд недочетов и недоработок. Требуется исправить и доработать,
согласно следующему плану.

При вычислении оклеиваемой поверхности мы не "портим" поле self.square. В нем так и остается
полная площадь стен. Ведь она может понадобиться, если состав списка wd изменится, и придется
заново вычислять оклеиваемую площадь.

Однако в классе не предусмотрено сохранение длин сторон, хотя они тоже могут понадобиться.
Например, если потребуется изменить одну из величин у уже существующего объекта. Площадь же
помещения всегда можно вычислить, если хранить исходные параметры. Поэтому сохранять саму
площадь в поле не обязательно.

Исправьте код так, чтобы у объектов Room были только четыре поля – width, lenght, height и wd.
Площади (полная и оклеиваемая) должны вычислять лишь при необходимости путем вызова методов.

Программа вычисляет площадь под оклейку, но ничего не говорит о том, сколько потребуется рулонов обоев.
Добавьте метод, который принимает в качестве аргументов длину и ширину одного рулона, а возвращает
количество необходимых, исходя из оклеиваемой площади.

Разработайте интерфейс программы. Пусть она запрашивает у пользователя данные и выдает ему площадь
оклеиваемой поверхности и количество необходимых рулонов.
"""


import math


class WinDoor:
    def __init__(self, x, y):
        self.square = x * y


class Room:
    def __init__(self, x, y, z):
        self.width, self.length, self.height = x, y, z
        self.wd = []

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    @property
    def square(self):
        return 2 * (self.width + self.length) * self.height

    def work_surface(self):
        square = self.square
        for i in self.wd:
            square -= i.square
        return square


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
