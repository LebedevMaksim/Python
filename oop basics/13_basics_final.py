# author: MLebedev
""" Практика по ООП. Final

https://younglinux.info/oopython/ooprogramm

"""


from random import randint


class Data:
    """Knowledge base. Elements can be retrieved by index."""
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Person:
    def __init__(self):
        self.oblivion = randint(0, 15)


class Teacher(Person):
    """The teacher must be able to transfer data from the knowledge base to the student or group"""
    def __init__(self):
        self.work = 0
        super().__init__()
        self.oblivion //= 2

    def teach(self, info, *pupil):
        for i in pupil:
            if randint(0, 100) > self.oblivion:
                i.take(info)
            self.work += 1


class Pupil(Person):
    """The student receives information and retains this knowledge. Maybe forget some data."""
    def __init__(self):
        self.knowledge = []
        super().__init__()

    def take(self, info):
        # Probability of getting knowledge
        if randint(0, 100) > self.oblivion:
            self.knowledge.append(info)


def main():
    knowledge = Data(
        'class',
        'object',
        'inheritance',
        'polymorphism',
        'encapsulation',
    )

    merlin = Teacher()

    pupils = [Pupil() for i in range(4)]

    for p in pupils:
        rndi = randint(0, len(knowledge.info)) - 1
        merlin.teach(knowledge[rndi], p)

    print(merlin.work)
    for p in pupils:
        print(p.knowledge)


if __name__ == "__main__":
    main()
