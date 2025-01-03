class Dog:
    def __init__(self):
        self.temperament = "loyal"

class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"

dog = Dog()
print(dog.temperament)

labrador = Labrador()
print(labrador.temperament)
