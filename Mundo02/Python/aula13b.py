'''
from time import sleep
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('ACABOU')

for c in range(0, 50, 2):
    print(c)


for c in range(3, 500, 3):
    if (c % 2) == 1:
        print(c)

print('TABUADA')
n=int(input('Digite o numero: '))
for c in range(0, 11, 1):
    print('{}x{}={}'.format(n,c,(n*c)))

r = 0
for c in range(6):
    n = int(input('digite um numero: '))
    if (n % 2) == 0:
        r = r + n
print('A soma é {}'.format(r))

t1 = float(input('Qual o primeiro termo? '))
r = float(input('Qual a razão? '))
s = 0
for c in range(1, 11):
    print(t1+s)
    s += r

num = int(input('Digite um numero: '))
p = 0
for c in range(1, num+1):
    if num % c == 0:
        p += 1
if p == 2:
    print('O numero {} é primo'.format(num))
else:
    print('O numero {} não é primo'.format(num))

frase = str(input('Digite uma frase: ')).strip()
edit = frase.lower().replace('', '')
invert = edit[::-1]
if edit == invert:
    print('A frase {} é um palíndromo.'.format(frase))
else:
    print('A frase {} não é um palíndromo.'.format(frase))

from datetime import date
print('POPULAÇÃO MAIOR!')
y = date.today().year
m = int(0)
mn = int(0)
for c in range(0,6):
    n = int(input('Digite o ano de nascimento: '))
    if y - n >= 18:
        m = m + 1
    else:
        mn = mn + 1
print('Dos citados, {} são menores.'.format(mn))
print('Dos citados, {} são maiores.'.format(m))

lista = []
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    lista.append(peso)
    lista.sort()
print('O menor peso citado foi {}'.format(lista[0]))
print('E o maior peso citado foi {}'.format(lista[-1]))

med = int()
maior = int()
mv = str()
qnt = int()
for c in range(1, 5):
    print('{}ª PESSOA: '.format(c))
    nome = str(input('Qual o seu nome? ')).strip().capitalize()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo? M/F ')).strip().upper()
    print('')
    med += idade/4
    if idade > maior and sexo == 'M':
        maior = idade
        mv = nome
    if idade < 20 and sexo == 'F':
        qnt += + 1
print('')
print('A média das idades é: {:.2f}'.format(med))
print('O homem mais velho se chama {}.'.format(mv))
print('{} mulheres tem menos de 20 anos.'.format(qnt))
'''