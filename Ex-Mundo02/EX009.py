print(11 * '=', 'LOJA MONZE', 11 * '=')

preco = float(input('Preço das compras: R$ '))

print('\nFormas de Pagamento:')
print('[ 1 ] À vista dinheiro/cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

escolha = int(input('Qual é a opção? '))

if escolha == 1:
    desconto = preco * 0.10
    novo_preco = preco - desconto
    print(f'Suas compras de R${preco:.2f} vão custar R${novo_preco:.2f} com 10% de desconto.')

elif escolha == 2:
    desconto = preco * 0.05
    novo_preco = preco - desconto
    print(f'Suas compras de R${preco:.2f} vão custar R${novo_preco:.2f} com 5% de desconto.')

elif escolha == 3:
    parcela = preco / 2
    print(f'Suas compras de R${preco:.2f} serão parceladas em 2x de R${parcela:.2f} sem juros.')

elif escolha == 4:
    pergunta = int(input('Quantas vezes deseja parcelar? '))
    juros = preco * 0.20
    novo_preco = preco + juros
    parcela = novo_preco / pergunta
    print(f'Suas compras de R${preco:.2f} vão custar R${novo_preco:.2f} com 20% de juros.')
    print(f'Parceladas em {pergunta}x de R${parcela:.2f}')

else:
    print('Opção inválida! Tente novamente.')
