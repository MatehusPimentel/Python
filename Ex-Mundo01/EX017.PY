from math import hypot 

co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente: '))

hi = hypot(co, ca)

print('A ipotenusa vai ser de {:.2f}'.format(hi))