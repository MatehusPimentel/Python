tabuada = int(input('Digite o numero que deseja ver a tabuada: '))

for n in range(1, 11):
    print('{} x {} = {}'.format(tabuada, n, tabuada * n))
