from itertools import count


class Person:
    count = 0
    def __init__(self) -> None:
        Person.count +=1
        self.count += 1
    @classmethod
    def printCount(cls):
        print(cls.count)
    def printCount(self):
        print(self.count)