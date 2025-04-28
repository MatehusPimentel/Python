salario = float(input('Informe o salário do funcionário: R$'))

if salario > 1250:
    aumento = (salario * 10) / 100

elif salario <=1250:
    aumento = (salario * 15) / 100

novo_salario = salario + aumento

print('Quem ganha R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,novo_salario))