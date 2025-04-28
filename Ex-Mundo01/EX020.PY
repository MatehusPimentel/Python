from random import shuffle

aluno = input('Informe o nome do aluno: ')
aluno1 = input('Informe o nome do aluno: ')
aluno2 = input('Informe o nome do aluno: ')
aluno3 = input('Informe o nome do aluno: ')

lista = [aluno,aluno1,aluno2,aluno3]

shuffle(lista)

print('A ordem é')
print(lista)
