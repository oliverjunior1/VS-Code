# What it do
""" class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p1 = Person("Tobias",25)
print(p1) """

# compare the two methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __regr__(self):
        return f"Person(self.name!r), age = {self.age}"

p1 = Person("Emil", 36)

print(p1)
print(repr(p1))