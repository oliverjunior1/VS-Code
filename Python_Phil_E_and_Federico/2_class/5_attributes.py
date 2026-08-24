'''Create a class called Cube, and assign the class attribute to it:

sides = 6

and the instance attribute:

color

Create a red_cube instance of that color.'''

class Cube:
    def __init__(self, sides, color):
        self.color = color
        self.sides = sides

red_cube = Cube(6, 'red')