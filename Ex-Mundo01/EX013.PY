salario = float(input('Informe o salário  R$'))

aumento = salario + (salario * 15 / 100)

print('O salário que era R${:.2f} com o aumento de 15% vai para R${:.2f}'.format(salario,aumento))
