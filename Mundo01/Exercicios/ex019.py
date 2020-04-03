'''import random
n1 = str(input('Digite o 1 Nome: '))
n2 = str(input('Digite o 2 Nome: '))
n3 = str(input('Digite o 3 Nome: '))
n4 = str(input('Digite o 4 Nome: '))
lista = [n1, n2, n3, n4]
es = random.choice(lista)
print('O Aluno escolhido é {}'.format(es))'''

from random import choice
n1 = str(input('Digite o 1 Nome: '))
n2 = str(input('Digite o 2 Nome: '))
n3 = str(input('Digite o 3 Nome: '))
n4 = str(input('Digite o 4 Nome: '))
lista = [n1, n2, n3, n4]
es = choice(lista)
print('O Aluno escolhido é {}'.format(es))