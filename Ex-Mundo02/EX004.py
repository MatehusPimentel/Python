from datetime import date
hj = date.today().year

ano = int(input('Digite o ano de nascimento: '))

idade = hj - ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, hj))

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE.')
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
elif idade < 18:
    print('Você ainda não tem 18 anos. Ainda faltam {} anos.'.format(18 - idade))
