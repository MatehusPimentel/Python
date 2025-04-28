print(5*'-='*5)
print('PA, 10 TERMOS'.center(45))
print(5*'-='*5)

termo = int(input('Primeiro termo: '))
razao = int(input('Razao: ')) 
decimo = termo + ( 10 - 1) * razao


for i in range(termo,decimo + razao,razao):
    print('{} '.format(i),end='→ ')
print('ACABOU')