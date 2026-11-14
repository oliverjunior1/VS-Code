""" 1. Enunciado do exercício
Você foi contratado para desenvolver um programa em Python que gerencie as vendas de uma loja.

O programa deverá:



4. Calcular o faturamento total da loja.
5. Mostrar os produtos com faturamento superior a R$ 500,00.
6. Exibir um relatório organizado na tela. """

# 1. Armazenar o nome dos produtos, preços e quantidades vendidas.
produtos = [
    {"nome": "Notebook", "preco": 3500.00, "quantidade": 3},
    {"nome": "Mouse", "preco": 80.00, "quantidade": 15},
    {"nome": "Teclado", "preco": 150.00, "quantidade": 8},
    {"nome": "Monitor", "preco": 1200.00, "quantidade": 5},
    {"nome": "Headset", "preco": 250.00, "quantidade": 10}
]

# 2. Calcular o faturamento de cada produto.
print(f"The product called {produtos[0]['nome']} was sold: {produtos[0]['preco']*produtos[0]['quantidade']}")
print(f"The product called {produtos[1]['nome']} was sold: {produtos[1]['preco']*produtos[1]['quantidade']}")
print(f"The product called {produtos[2]['nome']} was sold: {produtos[2]['preco']*produtos[2]['quantidade']}")
print(f"The product called {produtos[3]['nome']} was sold: {produtos[3]['preco']*produtos[3]['quantidade']}")
print(f"The product called {produtos[4]['nome']} was sold: {produtos[4]['preco']*produtos[4]['quantidade']}")

# 3. Identificar o produto mais vendido.