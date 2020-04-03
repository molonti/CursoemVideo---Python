cont = 0
conth = 0
contm = 0
print('-' * 35)
print('Programa de Cadastro de Pessoas')
while True:
    print('CADASTRO DE PESSOA')
    print('-' * 35)
    idade = int(input(('IDADE: ')))
    if idade >= 18:
        cont += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()
        if sexo == 'M':
            conth += 1
        elif idade < 20 and sexo == 'F':
            contm += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-' * 35)
print(f'TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {cont}')
print(f'TOTAL DE HOMENS CADASTRADOS: {conth}')
print(f'TOTAL DE MULHERES COM MENOS DE 20 ANOS: {conth}')
print('-' * 35)
print('TERMINO DO PROGRAMA')
