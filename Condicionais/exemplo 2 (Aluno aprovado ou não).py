nome = str(input('Digite o seu nome: '))
nota1 = int(input('Digite a sua primeira nota: '))
nota2 = int(input('Digite a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Parabéns, {}! Você foi aprovado e sua média foi {}'.format(nome, media))
else:
    print('Sinto muito, {}. Você foi reprovado e sua média foi {}'.format(nome, media))
print('--FIM--')