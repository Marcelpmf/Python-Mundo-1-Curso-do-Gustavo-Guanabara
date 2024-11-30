import math

cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))

cat_opostosoma = math.pow(cat_oposto,2)
cat_adjacentesoma = math.pow(cat_adjacente,2)
hipotenusa = math.sqrt(cat_adjacentesoma + cat_opostosoma)



print('A hipotenusa é igual a: {:.2f}'.format(hipotenusa))

#cateto oposto
#cateto adjacente
#hipotenusa
#hipotenusa² = adjacente² + oposto²

# ou #

hiporapido = math.hypot(cat_oposto, cat_adjacente)
print('A hipotenusa é igual a: {:.2f}'.format(hiporapido))


