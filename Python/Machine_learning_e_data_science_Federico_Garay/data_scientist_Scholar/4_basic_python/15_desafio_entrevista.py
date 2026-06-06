import pandas as pd
vendas = [100, 200, 300, 400, 500]
sr = pd.Series(vendas)
# Calcule total.
print(sr.sum())

# Calcule média.
print(sr.mean())

# Filtre vendas acima da média.
print(sr[sr>sr.mean()])

# Ordene do maior para o menor.
print(sorted(vendas, reverse=True))

# Aplique desconto de 10%.