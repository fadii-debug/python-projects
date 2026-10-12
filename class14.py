# OOP
# class
# object
# methods/function
# four pillars-----inheritance, encapsulation, polymorphism, abstraction
# polymorphism---- one function behave differently for multiple class

class Dog:
    def sit(self):
        print("Dog is sitting")

class Cat:
    def sit(self):
        print("Cat is sitting")

obj1=Dog()
obj2=Cat()

# function, parameters
def greet(animal):
    return(animal.sit())

greet(obj1)
greet(obj2)