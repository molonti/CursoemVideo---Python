from math import sin,cos,tan,radians
ang = float(input('Digite o angulo que deseja saber o seno cosseno e tangente: '))
ang1 = radians(ang)
seno = sin(ang1)
cose = cos(ang1)
tang = tan(ang1)
print(f'Com o angulo de {ang}º, o seno é {seno:.2f}, o cosseno é {cose:.2f} e a tangente é {tang:.2f}')

