soma = 0
qtd = 0 

for vezes in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(vezes)))
    if n % 2 == 0:
        soma += n
        qtd += 1

print('Voce informo {} numeros Pares e a soma foi {}'.format(qtd,soma))


