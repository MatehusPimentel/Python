numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para converter:')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

escolha = int(input('Sua escolha: '))

if escolha == 1:
    print('Convertendo {} para binário é igual a {}'.format(numero, bin(numero)[2:]))

elif escolha == 2:
    print('Convertendo {} para octal é igual a {}'.format(numero, oct(numero)[2:]))

elif escolha == 3:
    print('Convertendo {} para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))

else:
    print('({}) Essa escolha não existe. \nTENTE NOVAMENTE.'.format(escolha))
