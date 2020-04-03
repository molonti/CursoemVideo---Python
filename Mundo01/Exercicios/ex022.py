nome = str(input('Digite um Nome: ')).strip()
print('Seu nome em Maiúsculo {}'.format(nome.upper()))
print('Seu nome em Minúsculas {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu Primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu Primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))


