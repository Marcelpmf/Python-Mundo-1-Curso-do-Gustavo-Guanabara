largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = (largura * altura)
#1l = 2m²
quantidade = area/2

print('A quantidade de tinta necessária pra pintar a parede será de {.:2f} litros'.format(quantidade))