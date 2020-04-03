from datetime import date
ano = int(input('Ano para Analizar, ou Digite 0 para Ano atual: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano é BISSEXTO'.format(ano))
if ano == 0:
    ano = date.today().year
else:
    print('O ano não é BIXESTO'.format(ano))

