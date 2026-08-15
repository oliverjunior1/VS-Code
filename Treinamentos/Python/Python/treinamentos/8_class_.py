class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} and the age is {self.age}!"

Son = Family("Joao", 15)
Daughter = Family("Mariane", 5)

print(Son)
print(Daughter)