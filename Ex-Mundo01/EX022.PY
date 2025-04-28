nome = str(input('Informe seu nome completo: ')).strip()


print('Seu nome com todas as letras maiúsculas é {}'.format(nome.upper()))


print('Seu nome com todas as letras minúsculas é {}'.format(nome.casefold()))


print('Seu nome tem {} letras (sem contar os espaços).'.format(len(nome.replace(" ", ""))))

print('Seu primeiro nome tem {} Letras'.format(nome.find(' ')))
