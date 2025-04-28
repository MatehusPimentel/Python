from random import randint

computador = randint(0, 10)
certo = False
tentativas = 0

print('Sou seu computador.')
print('Estou a fim de jogar um jogo. Estou pensando em um número entre 0 e 10.')
print('Consegue descobrir qual é?')

while not certo:
    resposta = int(input('Qual é o número? '))
    tentativas += 1
    if resposta == computador:
        certo = True
    
    else:
        if resposta < computador:
            print('Mais... tente de novo.')
        elif resposta > computador:
            print('Menos... tente de novo.')

print('Parabéns! Você acertou!')
print(f'Você tentou {tentativas} vezes.')

