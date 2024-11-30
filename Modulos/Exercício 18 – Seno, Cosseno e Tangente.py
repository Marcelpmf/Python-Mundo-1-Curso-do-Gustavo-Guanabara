import math

angulo = float(input('Digite o angulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))




#import math

#cat_oposto = float(input('Digite o valor do cateto oposto: '))
#cat_adjacente = float(input('Digite o valor do cateto adjacente: '))

#cat_opostosoma = math.pow(cat_oposto,2)
#cat_adjacentesoma = math.pow(cat_adjacente,2)
#hipotenusa = math.sqrt(cat_adjacentesoma + cat_opostosoma)

#seno = cat_oposto/hipotenusa
#cosseno = cat_adjacente/hipotenusa
#tangente = cat_oposto/cat_adjacente



#print('O seno é igual a: {:.2f}'.format(seno))
#print('O cosseno é igual a: {:.2f}'.format(cosseno))
#print('O tangente é igual a: {:.2f}'.format(tangente))

# seno = cateto oposto / hipotenusa
# cosseno = cateto adjacente / hipotenusa
# tangente = cateto oposto / cateto adjacente

