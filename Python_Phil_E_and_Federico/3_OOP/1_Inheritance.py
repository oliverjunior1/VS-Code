'''Create a class called Person, which has the following instance attributes: name, age. Create another class, Student, 
which inherits these attributes from the first.'''

class Person:
    def __init__(self, place, age):
        self.place = place
        self.age = age


class Anapolino(Person):
    pass

Joao = Anapolino("Primavera", 35)

print(f"Joao live in {Joao.place} and has {Joao.age} years old.")



