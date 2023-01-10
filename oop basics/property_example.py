class Student:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        if 0 <= s <= 100:
            self._score = s
        else:
            raise ValueError('The score must be between 0 ~ 100!')


Yang = Student()

Yang.score = 99
print(Yang.score)
# 99

Yang.score = 999
# ValueError: The score must be between 0 ~ 100!
