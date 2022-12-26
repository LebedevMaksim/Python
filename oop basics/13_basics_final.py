# author: MLebedev
""" Практика по ООП. Final

https://younglinux.info/oopython/ooprogramm



"""


class Data:
    """Knowledge base. Elements can be retrieved by index."""
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Teacher:
    """The teacher must be able to transfer data from the knowledge base to the student or group"""
    def __init__(self):
        self.work = 0

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1


class Pupil:
    """The student receives information and retains this knowledge. Maybe forget some data."""
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)


def main():
    pass


if __name__ == "__main__":
    main()
