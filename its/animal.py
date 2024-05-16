from abc import ABC, abstractmethod

class Animal(ABC): 

    def __init__(self, name: str, age: int):
        super().__init__()

        self.name: str = name
        self.age: int = age

    @abstractmethod
    def verso():
        pass

class Cat(Animal):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def verso():
        print("Meow!")

class Dog(Animal):

    def __init__(self, name: str, age: int):
        super().__init__()

    def verso(self):
        print("Bau!")

class Horse(Animal):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)()

    def verso(self):
        print("Hyhyhyhy!")

cane_1: Dog = Dog("Fido", 3)
cavallo_1: Horse = Horse("Spirit", 10)