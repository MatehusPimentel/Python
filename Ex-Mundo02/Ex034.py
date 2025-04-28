maior1000 = 0
nome = ''
barato = 0
cont = 0
total = 0

print('=' * 40)
print(f'{"LOJAS MONZE":^40}')
print('=' * 40)

while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco

    pergunta = input('Quer continuar? [S/N] ').upper().strip()

    if preco > 1000:
        maior1000 += 1

    if cont == 1:
        barato = preco
        nome = produto
    else:
        if preco < barato:
            barato = preco
            nome = produto

    while pergunta not in 'SN':
        pergunta = input('Resposta inválida. Quer continuar? [S/N] ').upper().strip()

    if pergunta == 'S':
        continue

    elif pergunta == 'N':
        break

print('=' * 40)
print(f'{"FIM DO PROGRAMA":^40}')
print('=' * 40)

print(f'O total das compras é de R${total}')
print(f'Temos {maior1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato é a {nome} custando R${barato}')
