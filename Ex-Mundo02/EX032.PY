from random import randint

vitoria = 0

print('Oi, sou seu computador!')
print('Vamos jogar outro jogo.')
print('Dessa vez é Ímpar ou Par!')

while True:

    escolha = input('Escolha: [I]mpar ou [P]ar? ').strip().upper()

    numero = int(input('Jogador: escolha o número: '))
    computador = randint(0, 10)

    print(f'Computador escolheu o número: {computador}')

    soma = numero + computador
    print(f'A soma foi {soma}.', end=' ')
    if soma % 2 == 0:
        print('Deu Par!')
    else:
        print('Deu Ímpar!')

    if escolha == 'P':
        if soma % 2 == 0:
            print('Jogador venceu!\n')
            vitoria += 1
        else:
            print('Computador venceu!')
            break

    elif escolha == 'I':
        if soma % 2 == 1:
            print('Jogador venceu!\n')
            vitoria += 1
        else:
            print('Computador venceu!')
            break

print(f'\nJogo encerrado! Vitórias consecutivas do jogador: {vitoria}')
