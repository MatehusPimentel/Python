valor = 0
vezes = 0

for n in range (1, 501, 2):
    if n % 3  == 0:
        valor += n
        vezes += 1

print('A soma de todos os {} valores é {}'.format(vezes,valor))
 
 
 
        # 
        # soma = sum(valor)
        # print(soma)