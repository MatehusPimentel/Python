while True:

    n = int(input('Informe a tabuada que deseja: '))

    if n < 0:
        break

    for i in range(1, 10+1):
        print(f'{n} X {i} = {n * i}')

print('O programa fechou')



























# while True:
#     numero = int(input('Digite a tabuada desejada: '))
#     if numero < 0:
#         break
#     else:
#         for i in range(1, 10+1):
#             print(f'{i} X {numero} = {i * numero}')

#         print('Desseja continuar?')
#         resposta = input('s para sim n para nao: ').upper().strip()

#         if resposta == 'N':
#             break

#         elif resposta == 'S':
            
#             for i in range(1, 10+1):
#                 print(f'{i} X {numero} = {i * numero}')

#         else:
#             print('Essa alternativa nao é valida')
#             print('tente de novo ')