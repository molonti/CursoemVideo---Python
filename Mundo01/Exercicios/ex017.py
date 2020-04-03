'''co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hi = (co **2 + ca ** 2) ** (1/2)
print('CO {}, CA {} temos a Hipotenusa {:.2f}'.format(co, ca, hi))'''

'''import math
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('Hipotenusa {:.2f}'.format(hi))'''

from math import hypot
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hi = hypot(co, ca)
print('Hipotenusa {:.2f}'.format(hi))
