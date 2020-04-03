print('Triangulos')
print('=' * 20)
m1 = float(input('Digtite uma Medida: '))
m2 = float(input('Digite outra Medida: '))
m3 = float(input('Digite outra Medida: '))
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print('As medidas {}, {} e {} podem formar um Triangulo'.format(m1, m2, m3))
else:
    print('As medidas {}, {} e {} não podem formar um Triangulo'.format(m1, m2, m3))
