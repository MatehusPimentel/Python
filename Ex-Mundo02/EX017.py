n = int(input('Infrome um numero: '))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f'O numero {n} nao é primo')
            break
        
    else:
        print(f'O numero {n} é primo')
