import random

numero = int(random.randint(0,5))

print(numero) # mas ai tem q tirar ne

aposta = input('Digite sua aposta (0 a 5): ')

if aposta == numero:
    print('ACERTOU')
else:
    print('ERROU')
print('--FIM--')

