
nome = str(input('Digite seu nome: ')).strip()

separador = nome.split()

print('Seu primeiro nome é {}'.format(separador[0]))

print('Seu ultimo nome é {}'.format(separador[len(separador)-1]))