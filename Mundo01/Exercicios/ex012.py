p = int(input('Digite o valor do Produto: R$ '))
d = int(input('Digite o desconto: '))
np = p - (p * d / 100)
print(' O produto de R$ {:.2f} com desconto de {}% ficara por R$ {:.2f}'.format(p, d, np))

