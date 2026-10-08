nota_1 = float(input("Coloque a primeira nota: "))
nota_2 = float(input("Coloque a segunda nota: "))
nota_3 = float(input("Coloque a terceira nota: "))

media = (nota_1 + nota_2 + nota_3)/3

if media >= 7.0:
    print("Excelente, aprovado e com mérito!")
elif media >= 5.0:
    print("Passou!")
else:
    print("Reprovado.")