class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 30)
p2 = Person("Linus", 30)

print(p1 == p2)