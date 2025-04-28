print(5 * '-= ', end='')
print('PA, 10 TERMOS'.center(30), end='')
print(' =-' * 5)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1

while cont <= 10:
    print(f'{termo}', end=' → ')
    termo += razao
    cont += 1

print('ACABOU')
