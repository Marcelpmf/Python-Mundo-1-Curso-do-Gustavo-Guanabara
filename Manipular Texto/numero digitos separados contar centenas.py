numero = int(input('Digite um numero: '))

unidade = numero // 1 % 10 # unidade
dezena = numero  // 10 % 10
centena = numero // 100 % 10
milhar = numero //  1000 % 10

# 0 a 9999 (4 digitos)
# dividir todos primeiros em listas e depois contar
# ou ja pegar os numeros divididos mas tem o problema dos digitos
# usar inteiro e nao string


print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))