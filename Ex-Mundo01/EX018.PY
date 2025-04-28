from math import radians,sin,cos,tan

angulo = float(input('Digite o angulo: '))

seno = sin(radians(angulo))

print('O angulo de {} tem o seno de {:.2f}'.format(angulo,seno))

coseno = cos(radians(angulo))

print('O angulo de {} tem o coseno de {:.2f}'.format(angulo,coseno))

tangente = tan(radians(angulo))

print('O angulo de {} tem o tangente de {:.2f}'.format(angulo,tangente))