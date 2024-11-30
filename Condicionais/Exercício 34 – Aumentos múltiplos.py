salario = float(input('Digite o salario: '))

if salario > 1250:
    print('O seu salario de R${:.2f} com o aumento de 10% ficara R${:.2f}'.format(salario,salario*1.10))
else:
    print('O seu salario de R${:.2f} com o aumento de 15% ficara R${:.2f}'.format(salario, salario * 1.15))