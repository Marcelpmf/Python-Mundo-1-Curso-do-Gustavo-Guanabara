distancia = float(input('Digite a distancia da viagem: '))

if distancia <= 200:
    passagem = distancia * 0.50
    print('Você irá pagar R${:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Você irá pagar R${:.2f}'.format(passagem))
print('--FIM--')