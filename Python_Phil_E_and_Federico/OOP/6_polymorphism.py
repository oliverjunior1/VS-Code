'''Sobrescrita de métodos (Override)
Imagine uma classe Animal com um método falar().
A classe Cachorro sobrescreve esse método para retornar "Au au".
A classe Gato sobrescreve para retornar "Miau".
Quando você chama falar() em cada objeto, o resultado muda conforme o tipo do animal.'''

class Animal:
    def falar():
        print("O animal fala")


class Cachorro(Animal):
    def falar():
        print("Au au")

class Gato(Animal):
    def falar():
        print("Miau")


Gato.falar()
Cachorro.falar()
Animal.falar()