'''import math
ang = float(input('Digite o Angulo: '))
seno = math.sin(math.radians(ang))
print('Angulo {} temos o Seno {:.2f}'.format(ang, seno))
coss = math.cos(math.radians(ang))
print('Angulo {} temos o Cosseno {:.2f}'.format(ang, coss))
tang = math.tan(math.radians(ang))
print('Angulo {} temos a Tangente {:.2f}'.format(ang, tang))'''

from math import radians, sin, cos, tan
ang = float(input('Digite o Angulo: '))
seno = sin(radians(ang))
print('Angulo {} temos o Seno {:.2f}'.format(ang, seno))
coss = cos(radians(ang))
print('Angulo {} temos o Cosseno {:.2f}'.format(ang, coss))
tang = tan(radians(ang))
print('Angulo {} temos a Tangente {:.2f}'.format(ang, tang))