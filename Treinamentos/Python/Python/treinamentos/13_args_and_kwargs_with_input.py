def mostrar_dados(*args, **kwargs):
    for num in args:
        print(num)

    print('\n Informações extras')

    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")

numeros = input('Digite números separados por espaços: ')
numeros = tuple(map(int, numeros.split()))

nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")

mostrar_dados(*numeros, nome = nome, cidade = cidade)