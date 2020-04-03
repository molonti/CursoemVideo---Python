nome = str(input('Digite seu nome Completo: ')).strip()
nome = nome.split()
print('Seu primeiro Nome é {}'.format(nome[0]))
print('Seu último Nome é {}'.format(nome[len(nome)-1]))

