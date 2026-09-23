def classificar_salario(salario):

    if salario >= 5000:
        return "Alto"

    elif salario >= 3000:
        return "Médio"

    else:
        return "Baixo"

nome = input("Nome: ")

try:
    idade = int(input("Idade: "))
    salario = float(input("Salário: "))

    print()
    print("===== CLIENTE =====")
    print("Nome:", nome)
    print("Idade:", idade)
    print("Salário:", salario)

    if idade >= 18:
        print("Maior de idade.")
    else:
        print("Menor de idade.")

    categoria = classificar_salario(salario)

    print("Categoria salarial:", categoria)

except ValueError:
    print("Digite valores numéricos válidos.")
