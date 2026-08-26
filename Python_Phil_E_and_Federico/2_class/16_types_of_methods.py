'''Create an instance method throw_arrow() that subtracts by -1 the number of arrows a Character 
instance has, which in turn has an instance attribute called arrows_amount (that stores a certain number).'''

class Character:
    arrows_amount = 50  # isso é um atributo da classe, compartilhado por todas as instâncias

    def __init__(self, name):
        self.name = name
        self.arrows = Character.arrows_amount  # isso cria um atributo de instância com a quantidade inicial

    def throw_arrow(self):
        # isso diminui a quantidade de flechas da instância
        self.arrows -= 1
        if self.arrows <= 0:
            print(f"{self.name}, você não tem mais flechas.")
        else:
            print(f"{self.name} lançou uma flecha, restam {self.arrows}.")

# Criando personagem
Link = Character("Link")

# Usando método de instância
Link.throw_arrow()  # isso imprime "Link lançou uma flecha, restam 49."
Link.throw_arrow()  # isso imprime "Link lançou uma flecha, restam 48."
Link.throw_arrow()
Link.throw_arrow()






