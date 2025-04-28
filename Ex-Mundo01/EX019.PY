from random import choice

aluno = input('Informe o nome do aluno: ')
aluno1 = input('Informe o nome do aluno: ')
aluno2 = input('Informe o nome do aluno: ')
aluno3 = input('Informe o nome do aluno: ')

lista = [aluno,aluno1,aluno2,aluno3]

sorteio = choice(lista)

print('O aluno escolhido é {}'.format(sorteio))