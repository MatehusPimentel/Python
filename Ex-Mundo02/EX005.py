n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

if media <= 5:
    print('Sua nota é {:.1f}'.format(media))
    print('Voce esta reprovado')

elif media <= 6.9:
    print('Sua nota é {:.1f}'.format(media))
    print('Voce esta de recuperacao')

elif 7 <= media <= 10:
    print('Sua nota é {:.1f}'.format(media))
    print('Voce esta aprovado')
