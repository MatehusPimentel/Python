import time

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
escolha = 0

while escolha != 5:
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
''')

    escolha = int(input('Qual você deseja escolher: '))
    
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma dos números {n1} e {n2} é igual a {soma}.')

    elif escolha == 2:
        multi = n1 * n2
        print(f'A multiplicação dos números {n1} e {n2} é igual a {multi}.')

    elif escolha == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}.')
        elif n2 > n1:
            print(f'O maior número entre {n1} e {n2} é {n2}.')
        else:
            print('Os dois números são iguais.')

    elif escolha == 4:
        print('Escolha novos números:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))

    elif escolha == 5:
        print('O programa acabou. Até a próxima! 👋')

    else:
        print('Essa opção é inválida. Tente novamente.')
    
    print('-' * 40)
    time.sleep(2)
