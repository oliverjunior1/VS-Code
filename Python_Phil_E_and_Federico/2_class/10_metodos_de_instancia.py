class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}" # isso usa o atributo

# Exemplo de uso:
joao = Pessoa("João")
print(joao.apresentar()) 
