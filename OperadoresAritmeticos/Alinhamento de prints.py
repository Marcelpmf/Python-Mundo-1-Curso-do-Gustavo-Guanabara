nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:=^20}'.format(nome)) #:^alinha


n1 =  int(input('Digite um numero: '))
n2 =  int(input('Digite outro numero: '))

print('A soma vale {}'.format(n1+n2)) #n precisa de variavel assim

#usa variavel se for usar depois

soma = n1 + n2
mult = n1 * n2
divisao = n1 / n2
divisaoI = n1 // n2
expo = n1 ** n2

print('\n')
print('a soma é {},\na multiplicação é {} \na divisão é {}'.format(soma, mult, divisao))

#end='>>>' ) pra botar no fim da linha

print('a divisao inteira é {}\na exponenciação é {}'.format(divisaoI,expo))