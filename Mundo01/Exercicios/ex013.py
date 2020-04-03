sal = float(input('Digite o Sálario: R$ '))
por = float(input('Digite o Aumento: % '))
ns = sal + (sal * por / 100)
print('O Salário de R$ {:.2f} com Aumento de {}%, ficará com R$ {:.2f}'.format(sal, por, ns))
