velocidade = int(input('Digite a velocidade do carro em Km/h: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO')
    print('VOCÊ VAI PAGAR R${:.2f} DE MULTA'.format(multa))
else:
    print('OK')
print('--FIM--')