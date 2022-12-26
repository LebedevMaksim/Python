"""The module stores objects of the WinDoor and Room classes"""


class WinDoor:
    """The class stores the properties of the "windows" and "doors" objects"""
    def __init__(self, x, y):
        self.square = x * y


class Room:
    """The class stores the properties of the "room" object"""
    def __init__(self, x, y, z):
        """A room is created with the dimensions"""
        self.width, self.length, self.height = x, y, z
        self.wd = []

    def add_wd(self, w, h):
        """A "WinDoor" object is added"""
        self.wd.append(WinDoor(w, h))

    @property
    def square(self):
        """Room area"""
        return 2 * (self.width + self.length) * self.height

    def work_surface(self):
        """The working area is calculated by subtracting the area of windows from the total area"""
        square = self.square
        for i in self.wd:
            square -= i.square
        return square


def main():
    pass


if __name__ == "__main__":
    main()
