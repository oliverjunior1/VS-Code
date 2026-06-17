""" 
import pandas as pd

dados = {
    'personagem': [
        'Hero',
        'Erik',
        'Veronica',
        'Serena',
        'Sylvando',
        'Jade',
        'Rab'
    ],
    'forca': [85, 78, 30, 35, 65, 90, 45],
    'aparencia': [80, 75, 70, 85, 95, 88, 60],
    'inteligencia': [70, 65, 98, 90, 72, 68, 95],
    'educacao': [75, 60, 85, 92, 80, 78, 99]
}

df = pd.DataFrame(dados)

df.to_csv('dados.csv', index=False)

print("Arquivo dados.csv criado com sucesso!")
 """

""" import csv

with  open('dados.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha) """

import csv

with open('saida.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(
        ['None', 'Salario']
    )

    escritor.writerow(
        ['Ana', 5000]
    )