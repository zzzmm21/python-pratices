from animal import Animal
class Cat(Animal):
    def __init__(self) -> None:
        super().setName("고양이")
        self.bulter =True
        pass
    # def printSound(self):
    #     print("야옹")