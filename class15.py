# abstracttion-----parent, child------complrx data hide
# from module import method, name
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

dog = Dog()
cat = Cat()
cow = Cow()
print(dog.make_sound())
print(cat.make_sound())
print(cow.make_sound())