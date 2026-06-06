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
maior_salario = sorted(funcionarios, key=lambda a:a['salario'])
print(maior_salario[-1])
# Menor salário.
# Média salarial.
# Funcionários acima da média.
# Funcionários ordenados por salário.