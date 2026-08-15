list_names = ['Joaquim', 'Daniela', 'João','Ivan', 'Amarildo']

big_names = list(filter(lambda a: len(a)>6, list_names))

print(big_names)