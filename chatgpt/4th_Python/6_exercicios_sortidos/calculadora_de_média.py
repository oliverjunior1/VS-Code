"""Exercício 1 — Calculadora de média (variáveis e operações matemáticas)
Objetivo: aprender a trabalhar com variáveis, entrada de dados (input) e operações matemáticas.

Enunciado:

Crie um programa que solicite duas notas de um aluno, calcule a média e informe se ele foi aprovado ou reprovado. Considere média mínima igual a 7."""

def media_de_um_aluno():
    nota1 = float(input("Coloque a nota 1, por favor:"))
    nota2 = float(input("Coloque a nota 2, por favor:"))
    media = (nota1 + nota2)/2
    if media >= 70:
        print(f"Você passou, parabéns. Sua media foi {media}!")
    else:
        print(f"Você precisa estudar mais, foi reprovado. Sua média foi {media}!")


media_de_um_aluno()