clientes_dicts = [
    {
        "nome": "Ana",
        "idade": 25,
        "salario": 3500,
        "cidade": "Goiânia"
    },
    {
        "nome": "Joao",
        "idade": 22,
        "salario": 5000,
        "cidade": "Anápolis"
    },
    {
        "nome": "Maria",
        "idade": 50,
        "salario": 4200,
        "cidade": "Belo Horizonte"
    },
    {
        "nome": "José",
        "idade": 59,
        "salario": 4900,
        "cidade": "Brasília"
    },
    {
        "nome": "Michel",
        "idade": 62,
        "salario": 3200,
        "cidade": "Rio de Janeiro"
    }
]

# 1. Mostrar todos os clientes
for cliente in clientes_dicts:
    print(cliente)

# 2. Mostrar apenas clientes maiores de idade
for cliente in clientes_dicts:
    if cliente["idade"] >= 18:
        print(cliente["nome"])

# 3. Calcular a média salarial
soma_salarios = 0

for cliente in clientes_dicts:
    soma_salarios += cliente["salario"]

media = soma_salarios / len(clientes_dicts)

print("Média salarial:", media)