class WinDoor:
    def __init__(self, x, y):
        self.square = x * y


class Room:
    def __init__(self, x, y, z):
        self.width, self.length, self.height = x, y, z
        self.wd = []

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    @property
    def square(self):
        return 2 * (self.width + self.length) * self.height

    def work_surface(self):
        square = self.square
        for i in self.wd:
            square -= i.square
        return square


def main():
    pass


if __name__ == "__main__":
    main()
