frase = str(input('Digite uma frase: ')).strip().upper() # pra contar todos os A e strip pra evitar espaços em brancos contados


print('A letra "a" aparecer {} vezes na frase'.format(frase.count('A')))

print('A letra "a" aparece pela primeira vez na posição {} da frase'.format(frase.find('A')+1)) # pra ficar melhor de entender ja q começa com 0

print('A letra "a" aparece pela ultima vez na posição {} da frase'.format(frase.rfind('A')+1))



