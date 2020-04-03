nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é Popular.')
elif nome in 'Ana Juliana':
    print('Belo nome Feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}')
