nota1 = float(input('Digite a Primeira Nota: '))
nota2 = float(input('Digite a Segunda Nota: '))
n = (nota1 + nota2) / 2
print(f'Você tirou {n}')
if n < 5.0:
    print('REPROVADO:')
elif n > 6.9:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
