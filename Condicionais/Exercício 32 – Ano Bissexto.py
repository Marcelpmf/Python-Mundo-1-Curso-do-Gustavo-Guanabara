from datetime import date

ano = int(input('Digite o ano ou digite 0 pra ver o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 and ano % 100 != 0 or ano % 400 == 400: # diferente de 0
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))