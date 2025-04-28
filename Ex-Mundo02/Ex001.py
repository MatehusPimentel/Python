valor_casa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Digite sua renda salarial: R$ '))
anos = int(input('Em quantos anos deseja pagar a casa: '))

parcelas = valor_casa / (anos * 12)
minimo = salario * 0.30 

print('Valor da prestação mensal: R$ {:.2f}'.format(parcelas))
print('30% do seu salário: R$ {:.2f}'.format(minimo))

if parcelas <= minimo:
    print('Empréstimo concedido! A prestação está dentro do limite permitido.')
else:
    print('Empréstimo negado! A prestação excede 30% do seu salário.')
