largura = float(input('Informe a altura da parede: '))
altura = float(input('Informe a largura da parede: '))

area =largura * altura

print('Sua parede tem a dimensao de {}X{} e a área de {}m²'.format(largura,altura,area))

tinta = area / 2 

print('para printar a parede precisa de {}l de tinta'.format(tinta))