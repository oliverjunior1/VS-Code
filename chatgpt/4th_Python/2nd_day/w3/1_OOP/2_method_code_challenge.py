# Create a class called Dog
class Dog:
# Add an __init__ method with parameters name and age, and store them as properties using self
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Au au"
# Create an object d1 of the Dog class with name "Buddy" and age 3
d1 = Dog("Buddy",3)

# Call the bark method on d1

print(d1.bark())