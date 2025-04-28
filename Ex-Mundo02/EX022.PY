sexo = input('Informe seu sexo: [M/F] ').strip().upper()

while sexo not in ('M', 'F'):
    print('Sexo inválido. Tente novamente.')
    sexo = input('Informe seu sexo: [M/F] ').strip().upper()

print(f'Sexo {sexo} registrado com sucesso!')

