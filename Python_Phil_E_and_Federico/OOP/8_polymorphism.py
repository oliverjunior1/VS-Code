class Carro:
    def mover(self):
        return "O carro está dirigindo"

class Barco:
    def mover(self):
        return "O barco está navegando"

class Aviao:
    def mover(self):
        return "O avião está voando"

veiculos = [Carro(), Barco(), Aviao()]

for v in veiculos:
    print(v.mover)