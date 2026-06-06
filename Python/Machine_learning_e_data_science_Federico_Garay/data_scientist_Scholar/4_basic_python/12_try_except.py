""" try:
    x = 10/0
except:
    print("Any nunber can't be divide for zero!") """

try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Digite apenas números.")