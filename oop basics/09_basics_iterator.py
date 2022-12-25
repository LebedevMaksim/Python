# author: MLebedev
""" Практика по ООП #9

https://younglinux.info/oopython/iterator

Напишите класс-итератор, объекты которого генерируют случайные числа в количестве и в диапазоне,
которые передаются в конструктор.

"""


from random import randint


class Randi:
    def __init__(self, count, start, stop):
        self.nums = []
        for i in range(count):
            self.nums.append(randint(start, stop))

    def __iter__(self):
        return NumIterator(self.nums)


class NumIterator:
    def __init__(self, nums):
        self.nums = nums

    def __iter__(self):
        return self

    def __next__(self):
        if not self.nums:
            raise StopIteration
        num = self.nums[0]
        del self.nums[0]
        return num


def main():
    rnd = Randi(7, 100000, 900000)

    for i in rnd:
        print(i)


if __name__ == "__main__":
    main()
