'''Sobrecarga de métodos (Overload)

Em algumas linguagens (como Java ou C++), você pode ter vários métodos com o mesmo nome, mas parâmetros diferentes.

Exemplo: uma função somar() que aceita dois inteiros ou duas strings.'''

def somar(a, b):
    return a + b

print(somar(2,3))
print(somar(2.5,3.5))
print(somar("Olá, ", "Mundo"))