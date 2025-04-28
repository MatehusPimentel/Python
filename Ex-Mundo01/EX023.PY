n = int(input('informe o numero: '))

unidade = n // 1 % 10
decena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10

print('O numero {}'.format(n))
print('Unidade: {}'.format(unidade))
print('centena: {}'.format(centena))
print('milhar: {}'.format(milhar))