vc = float(input('Qual o Valor da Casa R$: '))
sal = float(input('Qual é o seu Salário R$: '))
anos = int(input('Quantos Anos: '))
meses = anos * 12
print('Meses', meses)
valorpar = vc / meses
salpar = sal - (sal * 30 / 100)
if salpar <= valorpar - (valorpar * 30 / 100):
    print('Financiamento Negado:')
else:
    print('Financiamento Aprovado:')
print(f'O Valor Parcela é R$ {valorpar:.2f} e o Salário menos 30 % R$ {salpar:.2f}')

