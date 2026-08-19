import pandas as pd

funcionarios = [
    {"nome": "Ana", "salario": 5000},
    {"nome": "Pedro", "salario": 7000},
    {"nome": "Julia", "salario": 4000},
    {"nome": "Carlos", "salario": 6000}
]

# 1. Média salarial:

df = pd.DataFrame(funcionarios)

media = df['salario'].mean()

print(media)

# 2. Calcule o total:
print(df["salario"].sum())

# 3. Maior salário:
print(df['salario'].max())

# 4. menor salário:
print(df["salario"].min())

# 5. Crie uma lista contendo apenas valores acima da média:
print(df[df["salario"]>df["salario"].mean()])

