from math import sqrt
ca = int(input('Cateto 1:'))
co = int(input('Cateto 2:'))
h1 = (ca**2)+(co**2)
h2 = sqrt(h1)
print(f'A sua hipotenusa é {h2:.3}')