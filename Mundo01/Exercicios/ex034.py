sal = float(input('Digite o sálario R$ '))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('O Novo salário é R$ {:.2f}'.format(novo))
