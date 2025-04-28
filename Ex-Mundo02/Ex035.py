print('=' * 40)
print(f'{"BANCO MONZE":^40}')
print('=' * 40)

valor = int(input('Valor do saque: R$'))

total = valor
cédula = 50 
total_cédulas = 0

print('\nContando as cédulas...')

while True:
    if total >= cédula:
        total -= cédula
        total_cédulas += 1
    else:
        if total_cédulas > 0:
            print(f'{total_cédulas} cédula(s) de R${cédula}')
        
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        
        total_cédulas = 0

        if total == 0:
            break

print('=' * 40)
print('Volte sempre ao BANCO MONZE!')
print('=' * 40)
