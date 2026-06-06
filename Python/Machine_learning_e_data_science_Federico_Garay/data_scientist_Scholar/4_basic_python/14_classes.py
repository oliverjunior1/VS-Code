""" class Funcionario:
    def __init__(self):
        self.nome = nome
        self.salario = salario


Ana = Funcionario('Ana', 5000)

print(Ana) """
import pandas as pd
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
df = pd.DataFrame(funcionarios)
print(df['salario'].mean())

# Funcionários acima da média.
print(df[df['salario']>df['salario'].mean()])
# Funcionários ordenados por salário.