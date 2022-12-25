# author: MLebedev
""" Практика по ООП #8

https://younglinux.info/oopython/staticmethod

Приведенный в конце урока пример плохой. Мы можем менять значения полей dia и h объекта за пределами класса
простым присваиванием (например, a.dia = 10). При этом площадь никак не будет пересчитываться. Также мы можем
назначить новое значение для площади, как простым присваиванием, так и вызовом функции make_area()
с последующим присваиванием. Например, a.area = a.make_area(2, 3). При этом не меняются высота и диаметр.

Защитите код от возможных логических ошибок следующим образом:

    Свойствам dia и h объекта по-прежнему можно выполнять присваивание за пределами класса. Однако при этом
    "за кулисами" происходит пересчет площади, т. е. изменение значения area.

    Свойству area нельзя присваивать за пределами класса. Можно только получать его значение.

Подсказка: вспомните про метод __setattr__(), упомянутый в уроке про инкапсуляцию.

"""


from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h

        return round(circle * 2 + side, 2)

    def __init__(self, dia, hi):
        self.diameter = dia
        self.high = hi
        self.__area = self.make_area(dia, hi)

    def __setattr__(self, key, value):
        if key == "diameter":
            self.__dict__[key] = value
            if "high" in self.__dict__:
                self.__area = self.make_area(self.diameter, self.high)
        elif key == "high":
            self.__dict__[key] = value
            if "diameter" in self.__dict__:
                self.__area = self.make_area(self.diameter, self.high)
        elif key == "_Cylinder__area":
            self.__dict__[key] = value
        else:
            raise AttributeError

    @property
    def info(self):
        return 'Diameter: ' + str(self.diameter) + ' high: ' + str(self.high) + ' area: ' + str(self.__area)


def main():
    c1 = Cylinder(2, 5)
    print(c1.info)

    c1.high = 10
    print(c1.info)

    c1.diameter = 4
    print(c1.info)

    c1._Cylinder__area = 10
    print(c1.info)


if __name__ == "__main__":
    main()
