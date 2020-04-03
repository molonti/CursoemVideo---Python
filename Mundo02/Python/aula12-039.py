from datetime import date
nasc = int(input('Informe o ano de seu nascimento: '))
hoje = date.today().year
idade = hoje - nasc
print (f'Você nasceu em {nasc}, então você tem {idade} anos de idade.')
if idade == 18:
    print('Você já está na idade para se alistar.')
elif idade < 18:
    print('Você ainda não precisa se alistar.')
    print(f'Faltam {18 -idade} anos, alistamento será em {hoje + (idade)}.')
else:
    print(f'Seu alistamento foi em {hoje -(idade - 18)}, há {idade - 18} anos.')
