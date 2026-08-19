""" idades = [18,20,25,30] #adicione um a todos os números da lista:

idades_plus_1 = [x+1 for x in idades]

print(idades_plus_1) """

# usando map
idades = [18,20,25,30]

idades_plus_1 = list(map(lambda x:x+1, idades))

print(idades_plus_1)



