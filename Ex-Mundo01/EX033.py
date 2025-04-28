n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

if n1 > n2 and n1 > n3:
    maior = n1

elif n2 > n1 and n2 > n3:
    maior = n2

elif n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1

elif n2 < n1 and n2 < n3:
    menor = n2

elif n3 < n1 and n3 < n2:
    menor = n3

print('O maior valoe é {}'.format(maior))

print('O menor valor é {}'.format(menor))