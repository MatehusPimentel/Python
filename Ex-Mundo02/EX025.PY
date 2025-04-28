n = int(input('Informe o número: '))
f = 1
contagem = n

print(f'{n}! = ', end='')

while contagem > 0:
    print(f'{contagem}', end=' ')
    print('x' if contagem > 1 else '= ', end='')
    f *= contagem
    contagem -= 1

print(f'{f}')
