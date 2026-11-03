"""Objetivo: trabalhar com listas (list) e laços de repetição (for).

Enunciado:

Crie um programa que armazene cinco produtos em uma lista e depois apresente todos os produtos cadastrados."""
produtos = []
i = 0;
while i <5:
    produto_digitado = input("Digite o produto para cadastrar: ")
    produtos.append(produto_digitado)
    i += 1
print(produtos)    