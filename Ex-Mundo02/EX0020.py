lista_pesos = []

for p in range(1,6):
    peso = float(input('peso da {}° pessoa: '.format(p)))
    lista_pesos.append(peso)

maiorpeso = max(lista_pesos)
menorpeso = min(lista_pesos)

print(f'Maior peso registrado: {maiorpeso}Kg')
print(f'Menor peso registrado: {menorpeso}Kg')





