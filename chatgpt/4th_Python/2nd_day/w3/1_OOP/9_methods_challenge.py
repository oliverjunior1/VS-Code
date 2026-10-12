# Create a class called Rectangle
class Rectangle:
    
# Add an __init__ method with width and height, and store them as properties
    def __init__(self,width,height):
        self.width = width
        self.height = height
# Add a method called area that returns the width multiplied by the height
    def area(self):
        return self.width * self.height

# Create an object r1 with width 5 and height 3
r1 = Rectangle(5,3)

# Print the area of r1
print(r1.area())