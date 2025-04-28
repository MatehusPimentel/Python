from datetime import date
ano_atual = date.today().year
maior = 0 
menor = 0

for i in range (7+1):
    nascimento = int(input('Infrome o ano de nascimento da {}° pessoa: '.format(i)))
    idade = ano_atual - nascimento

    if idade < 21:
        print('voce e menor de idade')
        menor += 1

    else:
        print('Voce ja é maior de idade')
        maior += 1

print(f'\nTotal de maiores de idade: {maior}')
print(f'Total de menores de idade: {menor}')
