clientes_dicts = [{
    "mome":"Ana",
    "idade":25,
    "salario":3500,
    "cidade":"Goiânia"
},
{
    "nome":"Joao",
    "idade":22,
    "salario":5000,
    "cidade": "Anápolis"
},
{
    "nome":"Maria",
    "idade":50,
    "salario":4200,
    "cidade":"Belo Horizonte"
},
{
    "nome":"José",
    "idade":59,
    "salario":4900,
    "cidade":"Brasília"
},
{
    "nome":"Michel",
    "idade":62,
    "salario":3200,
    "cidade":"Rio de Janeiro"
}]

# 1 mostrar todos os clientes
print(clientes_dicts)

# mostrar apenas maiores de idade
for chave in clientes_dicts.idade:
    if chave['idade'] >= 18:
        print(chave['nome'])

