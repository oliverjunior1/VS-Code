# Create a class called Car
class Car:

# Add an __init__ method with a brand parameter, and store it as a property
    def __init__(self, brand):
        self.brand = brand
    
# Add a method called show that prints the brand
    def show(self):
        print(self.brand) 
    
# Create an object c1 of the Car class with brand "Ford"
c1 = Car("Ford")

# Call the show method on c1
c1.show()