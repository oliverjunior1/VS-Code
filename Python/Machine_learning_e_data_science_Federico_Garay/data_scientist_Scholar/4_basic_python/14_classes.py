""" class Funcionario:
    def __init__(self):
        self.nome = nome
        self.salario = salario


Ana = Funcionario('Ana', 5000)

print(Ana) """

funcionarios = [
    {"nome":"Ana","salario":5000},
    {"nome":"Pedro","salario":7000},
    {"nome":"Julia","salario":4000},
    {"nome":"Carlos","salario":6000}
]

# Maior salário.
salario = sorted(funcionarios, key=lambda a:a['salario'])
print(salario[-1])

# Menor salário.
print(salario[1])

# Média salarial.
# Funcionários acima da média.
# Funcionários ordenados por salário.