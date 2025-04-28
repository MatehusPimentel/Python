velocidade = int(input('Informe a velocidade do carro: '))

limite = 80
multa = 7 

if velocidade > limite:
    km_acima = velocidade-limite
    valor = km_acima * multa
    print('Excedeu o limite permitido que é de 80Km/h')
    print('Deve pagar uma multa de R${}'.format(valor))
else:
    print('tenha um bom dia')