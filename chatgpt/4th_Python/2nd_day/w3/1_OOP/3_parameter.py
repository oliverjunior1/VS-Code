""" class Person: #class
    def __init__(self, name, age):
        self.name = name #atributos
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)


p1 = Person("Emil", 25)
p1.greet()
print(p1.age, p1.name) """

""" class Person:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname() """

""" class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def greet(abc):
        print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet() """

""" class Car:
    def __init__(self, brand, model, year):
        self.brand =brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")


car1 = Car("Toyota", "Corolla", 2020)
car1.display_info() """