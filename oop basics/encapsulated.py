# author: MLebedev
""" Практика по ООП #5

Разработайте класс с "полной инкапсуляцией", доступ к атрибутам которого и изменение данных
реализуются через вызовы методов. В объектно-ориентированном программировании принято имена
методов для извлечения данных начинать со слова get (взять), а имена методов, в которых
свойствам присваиваются значения, – со слова set (установить).
Например, get_field, set_field.
"""


class A:
    def __init__(self, value):
        self.__value = value

    def __setattr__(self, key, value):
        if key == "_A__value":
            self.__dict__[key] = value
        else:
            raise AttributeError

    def set_value(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value


def main():
    a = A(0)

    print(a.value)

    a.set_value(10)
    print(a.value)

    a.set_value(a.value * 5)
    print(a.value)

    print(a.__dict__)

    print(a._A__value)

    a._A__value = 22
    print(a.value)

    a.__value = 333
    print(a.value)


if __name__ == '__main__':
    main()
