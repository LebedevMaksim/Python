# author: MLebedev
""" Практика по ООП #4

В качестве практической работы попробуйте самостоятельно перегрузить оператор сложения.
Для его перегрузки используется метод __add__(). Он вызывается, когда объекты класса, имеющего
данный метод, фигурируют в операции сложения, причем с левой стороны. Это значит,
что в выражении a + b у объекта a должен быть метод __add__(). Объект b может быть чем угодно,
но чаще всего он бывает объектом того же класса. Объект b будет автоматически передаваться
в метод __add__() в качестве второго аргумента (первый – self).

Отметим, в Python также есть правосторонний метод перегрузки сложения - __radd__().

Согласно полиморфизму ООП, возвращать метод __add__() может что угодно. Может вообще ничего
не возвращать, а "молча" вносить изменения в какие-то уже существующие объекты. Допустим,
в вашей программе метод перегрузки сложения будет возвращать новый объект того же класса.
"""


class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, add_):
        return A(self.value + add_)


def main():
    a = A(5)
    b = a + 5

    print(b, b.value, sep='\n')


if __name__ == '__main__':
    main()
