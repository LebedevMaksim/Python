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
        self.knowledge = set()
        super().__init__()

    def take(self, info):
        # Probability of getting knowledge
        if randint(0, 100) > self.oblivion:
            self.knowledge.add(info)


def learning_cycle(data, teacher, pupils):
    for p in pupils:
        rndi = randint(0, len(data.info)) - 1
        teacher.teach(data[rndi], p)


def oblivion_cycle(data, pupils):
    for p in pupils:
        if p.oblivion > randint(0, 100):
            # Get new knowledge
            rndi = randint(0, len(data.info)) - 1
            p.take(data[rndi])
        else:
            # Same oblivion
            rndi = randint(0, len(p.knowledge)) - 1
            if rndi > 0:
                p.knowledge.discard(rndi)


def main():
    knowledge = Data(
        'class',
        'object',
        'inheritance',
        'polymorphism',
        'encapsulation',
    )

    merlin = Teacher()

    pupils = [Pupil() for i in range(7)]

    # Study period
    for i in range(5):
        # Time for knowledge
        learning_cycle(knowledge, merlin, pupils)
        # Time for rest
        oblivion_cycle(knowledge, pupils)

    print(merlin.work)
    for p in pupils:
        print(p.knowledge)


if __name__ == "__main__":
    main()
