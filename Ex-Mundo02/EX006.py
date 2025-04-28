from datetime import date
atual = date.today().year

ano = int(input('Digite p seu ano de nascimento: '))
idade = atual - ano

if idade <= 9:
    print('Categoria: Mirim')

elif idade <= 14:
    print('Categoria: Infantil')

elif idade <= 19:
    print('Categoria: Junior')

elif idade <= 25:
    print('Categoria: Sênior')

else:
   print('Categoria: Master')
