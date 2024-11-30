import math
import emoji
#from math import sqrt, ceil, floor (importa so a funcao de achar raiz e arrendondar)

numero = int(input('Digite um numero: '))
raiz = math.sqrt(numero)

print('A raiz de {} é igual a {}'.format(numero, raiz))
print('A raiz de {} é igual a {}'.format(numero, math.ceil(raiz))) # arrendonda pra cima
print('A raiz de {} é igual a {}'.format(numero, math.floor(raiz))) # arrendonda pra baixo


print(emoji.emojize("Olá, mundo :robot:"))