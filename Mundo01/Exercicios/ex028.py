from random import randint
from time import sleep
pc = randint(0, 5)
print('=' * 20)
print('Escolha um numero de 0 a 5')
print('=' * 20)
jg = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jg == pc:
    print('ACERTOU.')
else:
    print('EU Pensei no {} e Ganhei e não era o {}'.format(pc, jg))

