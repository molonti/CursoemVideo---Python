'''sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo M/F: ')).upper()
print('Sexo digitado {}'.format(sexo))

from random import randint
from time import sleep
print('Digite um Número de 0 a 10...')
sleep(1)
print('TENTE ACERTAR')
tentativas = 0
numero = -1
numeroPensado = randint(0, 10)
while numero != numeroPensado:
    numero = int(input('Foi o número: '))
    tentativas += 1
    if numero != numeroPensado:
        print('Errou!')
    else:
        print('VOCÊ ACERTOU!')
print('O número pensado foi o {} e você tentou {} vezes'.format(numeroPensado, numero))


i = int(input("Digite um numero: "))
o = int(input("Digite outro numero: "))
t = int(input(' Escolha uma opcao:
    [1] Somar
    [2] Multiplicar
    [3] Maior numero
    [4] Novos numeros
    [5] Sair do programa
     Digite uma opcao: '))
while t !=5:
    if t == 1:
        print("O resultado da soma e: {}".format(i+o))
        break
    elif t == 2:
        print("O resultado da multiplicao e: {}".format(i*o))
        break
    elif t == 3:
        if i > o:
            print("O Maior numero e: {}".format(i))
        if o > i:
            print("O maior numero e: {}".format(o))
        else:
            print("Resultado invalido ou numeros iguais")
        break
    elif t == 4:
        i = int(input("DIgite outro numero: "))
        o = int(input("Digite outro numero"))
        t = int(input(' Escolha uma opcao:
    [1] Somar
    [2] Multiplicar
    [3] Maior numero
    [4] Novos numeros
    [5] Sair do programa
    Digite uma opcao: '))

n1 = int(input('Fatorial: '))
x = fatorial = 1
aux = n1
while x < n1:
    fatorial = aux*x
    print('{} * {} = {}'.format(n1, x, fatorial))
    aux = fatorial
    x += 1
print(fatorial)


n1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: :'))
c = 0
while c < 10:
    print(n1)
    n1 = n1 + raz
    c += 1

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
contador = 10
n = 0
while cont <= contador:
    print('{} » '.format(termo), end='')
    termo += razao
    cont += 1
    n += 1
    if cont == contador+1:
        print('PAUSA')
        contador = int(input('Quantos termos você quer mostrar a mais? '))
        cont = 1
print('Progressão finalizada com {} termos mostrados.'.format(n))


n = int(input('Quantos números fibonacci devem aparecer: '))
c = 0
f = 0
r = f
while c != n:
    if c == 0:
        print(f)
        f = f + 1
    else:
        print(f)
        f = f + r
        r = f - r
    c = c + 1

n = int(input('Informe um número inteiro: '))
cont = 0
cont1 = 0
while n != 999:
    if n == 999:
        cont = cont
    else:
     cont = cont + n
     cont1 += 1
    n = int(input('Informe um número inteiro: '))
print('Soma entre o números digitados antes do 999: {}'.format(cont))
print('Total de números digitados antes do 999: {}'.format(cont1))

checar = 's'
maior = 0
menor = 0
media = 0
i = 0
while checar == 's':
    num = int(input('Digite um número:'))
    media += num
    if i == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    else:
        if num < menor:
            menor = num
    i+=1
    checar = str(input('Quer continuar a digitar [s/n]:'))
    if checar != 's':
        while checar != 'n':
            checar = str(input('Quer continuar a digitar [s/n]:'))
            if checar == 's':
                break
media = media / i
3print(f'A média dos valores lidos foi: [{media}]')
print('-'*50)
print('O maior número [{:.1f}]. O menor número [{:.1f}].'.format(maior, menor))
'''
