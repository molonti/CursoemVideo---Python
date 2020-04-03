while True:
    valor = int(input('INFORME O VALOR DO SAQUE: R$ '))
    while valor < 1:
        valor = int(input('VALOR INVÁLIDO! DIIGTE NOVAMENTE: R$ '))
    a = valor % 50
    cinquenta = (valor - a) / 50
    b = a % 20
    vinte = (a - b) / 20
    c = b % 10
    dez = (b - c) / 10
    d = c % 1
    um = (c - d) / 1
    break
print('{} notas de R$50'.format(int(cinquenta)))
print('{} notas de R$20'.format(int(vinte)))
print('{} notas de R$10'.format(int(dez)))
print('{} notas de R$1'.format(int(um)))
