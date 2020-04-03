#nome = input('Qual o seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n2 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira é {} e a potência {}'.format(di, e))
