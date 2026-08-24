def return_distincts(x, y, z):
    lista_somada =[x, y, z]
    lista_ordenada = sorted(lista_somada)
    if sum(lista_somada) > 15:
        return max(lista_somada)
    elif sum(lista_somada) < 10:
        return min(lista_somada)
    else:
        return lista_ordenada[1]

print(return_distincts(5,3,2))