'''Create a class called Character, and assign the following class attribute to it:

real = False

Create an instance called harry_potter with the following instance attributes:

species = "Human"

magical = True

age = 17'''

class Character:
    def __init__(self, real, species, magical, age):
        self.real = real
        self.species = species
        self.magical = magical
        self.age = age


harry_potter = Character(False, 'Human', True, 17)