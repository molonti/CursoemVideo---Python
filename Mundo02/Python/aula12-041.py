from datetime import date
nasc = int(input('Digite o ano de Nascimento: '))
hoje = date.today().year
idade = hoje - nasc
print(f'Sua idade é {idade}:')
if idade <= 9 :
    print('MIRIM')
elif idade <= 14 :
    print('INFANTIL')
elif idade <= 19 :
    print('JUNIOR')
elif idade <= 20 :
    print('SENIOR')
else:
    print('MASTER')
