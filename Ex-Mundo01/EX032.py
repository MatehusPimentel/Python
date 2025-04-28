from datetime import datetime

ano = int(input('Informe o ano (0 para o ano atual): '))

if ano == 0:
    ano = datetime.now().year

print(f'Analisando o ano: {ano}')

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')

