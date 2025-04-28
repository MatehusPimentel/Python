qtd_mulheres = 0
maior_idade = 0
qtd_homens = 0  

print('-' * 40)
print(f'{"CADASTRO DE PESSOAS":^40}')
print('-' * 40)

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper().strip()

    while sexo not in 'MF':
        sexo = input('Entrada inválida. Sexo: [M/F] ').upper().strip()

    if idade >= 18:
        maior_idade += 1
    
    if sexo == 'M':
        qtd_homens += 1

    if sexo == 'F' and idade < 20:
        qtd_mulheres += 1

    print('-' * 40)
    
    pergunta = input('Quer continuar? [S/N] ').upper().strip()
    while pergunta not in 'SN':
        pergunta = input('Resposta inválida. Quer continuar? [S/N] ').upper().strip()

    if pergunta == 'N':
        break

print('\n' + '=' * 40)
print(f'{"RESUMO DO CADASTRO":^40}')
print('=' * 40)
print(f'Total de pessoas com 18 anos ou mais: {maior_idade}')
print(f'Total de homens cadastrados: {qtd_homens}')
print(f'Total de mulheres com menos de 20 anos: {qtd_mulheres}')
print('=' * 40)
print(f'{"FIM DO PROGRAMA":^40}')
print('=' * 40)
