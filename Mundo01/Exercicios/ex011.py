la = float(input('Digite a Largura da Parede: '))
al = float(input('Digite a Altura da Parede: '))
area = la * al
print('Parede de {} x {} tem área de {} m2'.format(la, al, area))
t = area / 2
print('Para está parede você usará {:.0f} litros de tinta'.format(t))
