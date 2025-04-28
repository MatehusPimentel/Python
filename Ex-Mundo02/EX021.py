idade_soma = 0
mais_velho = ''
idade_velho = 0
qtd_mulher = 0
qtd20 = 0
for i in range(1, 5):
    print('-' * 5, f'{i}° pessoa', '-' * 5)
    
    nome = input('Nome: ').strip().upper()
    idade = int(input('Idade: '))
    sexo = input('[M/F]: ')

    idade_soma += idade

    if sexo in 'Mm':
        if idade > idade_velho:
            idade_velho = idade          
            mais_velho = nome            

    if sexo in 'Ff':
        if idade < 20:
            qtd20 += 1
            qtd_mulher += 1

media = idade_soma / i

print(f'\nA média das idades do grupo é de {media:.2f} anos')
print(f'O homem mais velho é {mais_velho} com {idade_velho} anos')
print(f'Ao todo são {qtd_mulher} mulheres, sendo {qtd20} com menos de 20 anos')

