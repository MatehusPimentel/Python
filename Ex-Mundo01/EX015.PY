dias = int(input('Quantos dias vai alugar: '))
km = float(input('Quantos Km foram andados: '))

valor = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(valor))