""" salarios = [5000, 3000, 7000, 4000]

# salarios_ordenados = sorted(salarios)
salarios_ordenados = sorted(salarios, reverse=True)

print(salarios_ordenados) """

funcionarios = [
    {"nome":"Ana","salario":5000},
    {"nome":"Pedro","salario":7000},
    {"nome":"Julia","salario":4000}
]

sorted_dict = sorted(funcionarios, key=lambda x:x['salario'])

print(sorted_dict)