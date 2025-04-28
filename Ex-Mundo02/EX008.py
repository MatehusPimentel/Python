peso = float(input('Infrome o peso: Kg'))
altura = float(input('Informe a altura: M'))
IMC = peso / (altura ** 2)

print(f'Seu IMC é: {IMC:.2f}')


if IMC < 18.5:
    print('Classificação: Abaixo do peso')
elif IMC < 25:
    print('Classificação: Peso normal')
elif IMC < 30:
    print('Classificação: Sobrepeso')
elif IMC < 35:
    print('Classificação: Obesidade grau 1')
elif IMC < 40:
    print('Classificação: Obesidade grau 2')
else:
    print('Classificação: Obesidade grau 3')
