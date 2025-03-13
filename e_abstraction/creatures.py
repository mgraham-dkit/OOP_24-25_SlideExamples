from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self):
        return "Bark!"


dog = Dog("Fido")
print(dog.make_sound())