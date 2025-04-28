from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('Suas Opções:')
print(''' 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

jogador = int(input('Qual é a sua escolha? '))

print(f'\nComputador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}\n' if jogador in [0, 1, 2] else '\nJogada inválida!\n')


if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:  
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
