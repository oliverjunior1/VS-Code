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
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
