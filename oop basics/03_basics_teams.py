# author: MLebedev
""" Практика по ООП #3

https://younglinux.info/oopython/inheritance

В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее
уникальный номер объекта, и свойство, в котором хранится принадлежность команде.
У солдат есть метод "иду за героем", который в качестве аргумента принимает
объект типа "герой". У героев есть метод увеличения собственного уровня.

В основной ветке программы создается по одному герою для каждой команды.
В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран.
У героя, принадлежащего команде с более длинным списком, увеличивается уровень.

Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.
"""


from random import randint


class Unit:
    def __init__(self, uid, team):
        self.uid, self.team = uid, team


class Solder(Unit):
    def __init__(self, uid, team, hero=None):
        super().__init__(uid, team)
        self.hero = hero

    def follow_hero(self, hero):
        self.hero = hero


class Hero(Unit):
    def __init__(self, uid, team, level=0):
        super().__init__(uid, team)
        self.level = level

    def level_up(self, num):
        self.level += num


class UID:
    def __init__(self):
        self.count = -1

    @property
    def new(self):
        self.count += 1
        return self.count


def main():
    heroes = []
    team_a = []
    team_b = []
    solder_count = 16

    uid = UID()

    heroes.append(Hero(uid.new, team_a))
    heroes.append(Hero(uid.new, team_b))

    for i in range(solder_count):
        if randint(1, 10) % 2:
            team_a.append(Solder(uid.new, team_a))
        else:
            team_b.append(Solder(uid.new, team_b))

    for i, team in enumerate((team_a, team_b)):
        print(f'Team {i + 1}: {len(team)} solders')

    if len(team_a) > len(team_b):
        heroes[0].level_up(1)
    elif len(team_a) < len(team_b):
        heroes[1].level_up(1)

    for hero in heroes:
        print(f'Hero id:{hero.uid}, level:{hero.level}')

    captain = heroes[0]
    follower = captain.team[randint(0, len(captain.team)) - 1]  # FIX ME (error if len == 0)
    follower.follow_hero(captain)

    print(f'Captain id: {captain.uid}, follower id: {follower.uid}')


if __name__ == '__main__':
    main()
