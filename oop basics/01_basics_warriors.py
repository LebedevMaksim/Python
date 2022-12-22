# author: MLebedev
""" Практика по ООП

https://younglinux.info/oopython/objects

Напишите программу по следующему описанию. Есть класс "Воин". От него создаются два экземпляра-юнита.
Каждому устанавливается здоровье в 100 очков. В случайном порядке они бьют друг друга. Тот, кто бьет,
здоровья не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. После каждого удара
надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья. Как только
у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
"""


from random import randint


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def get_damage(self, damage):
        if self.health > 0:
            self.health -= damage

    @property
    def is_alive(self):
        return True if self.health > 0 else False


def main():
    warriors = []
    damage = 35

    warriors.append(Warrior('Odin'))
    warriors.append(Warrior('Zeus'))

    while warriors[0].is_alive and warriors[1].is_alive:
        aggressor = randint(1, 10) % 2
        print(warriors[aggressor].name, 'атакует.', warriors[aggressor-1].name, 'получает урон:', damage)
        warriors[aggressor-1].get_damage(damage)

    for i in range(len(warriors)):
        print(f'{warriors[i].name} мертв' if not warriors[i].is_alive
              else f'{warriors[i].health} HP осталось у {warriors[i].name}')


if __name__ == '__main__':
    main()
