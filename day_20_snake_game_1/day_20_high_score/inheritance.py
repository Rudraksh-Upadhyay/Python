class Animal:
    def __init__(self):
        self.legs = 2
        self.eyes = 2

    def breathe(self):
        print("inhale exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("swimming")

    def breathe(self):              #OVER RIDING
        super().breathe()
        print("he is breathing")


my_fish = Fish()
print(my_fish.eyes)
print(my_fish.legs)
my_fish.breathe()
my_fish.swim()