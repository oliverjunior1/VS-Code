# Crie um programa que solicite um número inteiro e informe se ele é par ou ímpar.

# solicitar o número
seu_numero = int(input("Coloque o número: "))

# verificar se ele é par ou impar
if seu_numero%2==0:
    print(f"Seu número {seu_numero} é par!")
else:
    print(f"Seu número {seu_numero} é impar.")
