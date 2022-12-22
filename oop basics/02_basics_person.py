# author: MLebedev
""" Практика по ООП #2

https://younglinux.info/oopython/init

Есть класс Person, конструктор которого принимает три параметра (не учитывая self) – имя, фамилию
и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.

У класса Person есть метод, который возвращает строку, включающую в себя всю информацию
о сотруднике.

Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …"
(вместо троеточия должны выводиться имя и фамилия объекта).

В основной ветке программы создайте три объекта класса Person. Посмотрите информацию о сотрудниках
и увольте самое слабое звено.

В конце программы добавьте функцию input(), чтобы скрипт не завершился сам, пока не будет
нажат Enter. Иначе вы сразу увидите как удаляются все объекты при завершении работы программы.
"""


from random import randint


class Person:
    def __init__(self, name, s_name, level=1):
        self.name, self.s_name, self.level = name, s_name, level

    def info(self):
        return self.name, self.s_name, self.level

    def __del__(self):
        print(f'До свидания, мистер {self.name} {self.s_name}')


def staf_info(staf):
    for i, person in enumerate(staf):
        print(f'{i + 1}:', *person.info())

def main():
    staf = []

    for name, s_name, level in (
            ('John', 'Snow', randint(0, 20)),
            ('Thomas', 'Anderson', randint(0, 20)),
            ('Sarah', 'Connor', randint(0, 20)),
                                ):
        staf.append(Person(name, s_name, level))

    staf_info(staf)

    for i in range(len(staf) - 1):
        if staf[i].level <= staf[i + 1].level:
            staf[i], staf[i + 1] = staf[i + 1], staf[i]

    staf.pop()

    input('\nPress any key to terminate.')


if __name__ == '__main__':
    main()
