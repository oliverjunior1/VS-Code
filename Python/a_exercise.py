'''
Descrição
Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes.

📌 Regras de desconto:

"DESCONTO10": 10% de desconto.
"DESCONTO20": 20% de desconto.
"SEM_DESCONTO": Sem desconto.
Entrada
Preço original do produto.
Código do cupom digitado.
Saída
Preço final após aplicar o desconto. Com duas casas decimais.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
100
DESCONTO10	90.00
200
DESCONTO20	160.00
50
SEM_DESCONTO	50.00
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

Os desafios apresentados aqui têm como objetivo principal exercitar os conceitos aprendidos e proporcionar um primeiro contato com lógica de programação. Caso não tenha experiência em programação, utilize o template disponível e preencha com os conceitos aprendidos. Para resetar o template, basta clicar em “Restart Code”.'''

# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:
if cupom in descontos:
    preco_final = preco * (1 - descontos[cupom])
else:
    preco_final = preco

# Saída
print(f"{preco_final:.2f}")
# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}
# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()


