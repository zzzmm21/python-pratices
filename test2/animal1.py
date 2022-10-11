from animal import Animal
from cat import Cat
from dog import Dog


an = Animal()
print(an.name)
an.__setattr__("name","?")

print(an.__dict__)
#  부모꺼 가져다 쓸 수 있음
cat= Cat()
cat.printSound()
print(cat.name)

dog = Dog()
dog.printSound()
print(dog.name)
