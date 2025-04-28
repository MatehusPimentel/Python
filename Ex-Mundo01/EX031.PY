dis = int(input('Informe a distancia da viagem Km: '))

if dis <=200:
    valor_km = 0.50
    total = dis * valor_km

else:
    valor_km = 0.45
    total = dis * valor_km


print(f'O valor da passagem é de R${total:.2f}')