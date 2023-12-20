class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"{self.name} is a {self.species}.")

class Mammal(Animal):
    def __init__(self, name, species, fur_color, num_legs):
        super().__init__(name, species)
        self.fur_color = fur_color
        self.num_legs = num_legs

    def give_birth(self):
        print(f"{self.name} is giving birth to live young.")

    def display_info(self):
        print(f"{self.name} is a {self.species} with {self.num_legs} legs and {self.fur_color} fur.")

class Bird(Animal):
    def __init__(self, name, species, beak_length, can_fly):
        super().__init__(name, species)
        self.beak_length = beak_length
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying.")
        else:
            print(f"{self.name} is not capable of flight.")

    def display_info(self):
        print(f"{self.name} is a {self.species} with a beak length of {self.beak_length} inches.")

class Fish(Animal):
    def __init__(self, name, species, scale_color, water_type):
        super().__init__(name, species)
        self.scale_color = scale_color
        self.water_type = water_type

    def swim(self):
        print(f"{self.name} is swimming in {self.water_type} water.")

    def display_info(self):
        print(f"{self.name} is a {self.species} with {self.scale_color} scales.")

mammal = Mammal("Bear", "Grizzly", "black-brown", 4)
mammal.give_birth()
mammal.display_info()

bird = Bird("Hen", "Home", 5, False)
bird.fly()
bird.display_info()

fish = Fish("GoldenFish", "Amphiprioninae", "yellow", "saltwater")
fish.swim()
fish.display_info()
