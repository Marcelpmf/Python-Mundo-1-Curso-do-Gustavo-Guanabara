km = float(input('Digite a quantidade de Km percorridos pelo carro: '))
dias = int(input('Digite a quantidade de dias que o carro esteve alugado: '))

# R$60 o dia
# R$0.15 x Km

pagar = (km*0.15) + (dias*60)

print('Preço total: R${:.2f}'.format(pagar))
