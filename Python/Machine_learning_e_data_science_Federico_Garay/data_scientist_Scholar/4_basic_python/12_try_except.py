""" try:
    x = 10/0
except:
    print("Any nunber can't be divide for zero!") """

""" try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Digite apenas números.") """

# Exercício 4
# Crie um programa que:
# peça salário
# trate erros de digitação

try:
    salario = float(input("Type your salary: "))
except:
    print('You need to put a number.')
