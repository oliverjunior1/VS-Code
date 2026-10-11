# Class
""" class MyClass:
    x = 5

print(MyClass.x) """

# Object
""" class MyClass:
    x = 5

p1 = MyClass() # object
print(p1.x) """

# Method, name and age
""" class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age) """

""" class Person:
    pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age) """

""" class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age) """

""" class Person: 
    def __init__(self, name, age= 18):
        self.name = name 
        self.age = age

p1 = Person("Emil") # Instance
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)
 """

""" class Person: # class
    def __init__(self, name, age, city, coutry):
        self.name = name # Attributos
        self.age = age 
        self.city = city
        self.coutry = coutry

    def andar(self): # Method
        return "A pessoa anda" 

p1 = Person("Linus", 30, "Oslo", "Norway") # Instance/Object

x = str(p1.andar())
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.coutry)
print(x) """

