funcionarios = [
    {"nome": "Ana", "salario": 5000},
    {"nome": "Pedro", "salario": 7000},
    {"nome": "Julia", "salario": 4000}
]

menor = min(funcionarios, key=lambda x:x['salario'])

print(menor)