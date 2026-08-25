class ContaBancaria:
    banco = "Banco Central" # atributo de classe

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    # Método de instância
    def depositar(self, valor):
        self.saldo += valor # altera o saldo
        return f"Depósito de {valor} realizado. Saldo atual: {self.saldo}"

    # Método de classe
    @classmethod
    def info_banco(cls):
        return f"Todas as contas pertencem ao {cls.banco}"

    # Método Estático
    @staticmethod
    def validar_valor(valor):
        return valor > 0


#----------------------EXEMPLOS DE USO --------------------------------

# Criando uma conta (instância)
conta1 = ContaBancaria("Joaquim", 100)

# Usando o método de instância
print(conta1.depositar(50))
# isso imprime "Depósito de 50 realizado: saldo atual: 150"

# Usando método de classe
print(ContaBancaria.info_banco())
# isso imprime "Todas as contas pertencem ao Banco Central"

#Usando método estático
print(ContaBancaria.validar_valor(-10))
# isso imprime false, porque o valor não é válido