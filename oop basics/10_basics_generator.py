# author: MLebedev
""" Практика по ООП #9

https://younglinux.info/oopython/generator

В задании к прошлому уроку требовалось написать класс-итератор, объекты которого
генерируют случайные числа в количестве и в диапазоне, которые передаются в конструктор.
Напишите выполняющую ту же задачу генераторную функцию. В качестве аргументов она должна
принимать количество элементов и диапазон.

"""


from random import randint


def num_generator(count, start, stop):
    for i in range(count):
        yield randint(start, stop)


def main():
    nums = num_generator(4, 100, 500)

    for i in nums:
        print(i)


if __name__ == "__main__":
    main()
