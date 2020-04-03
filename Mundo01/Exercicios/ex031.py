km = int(input('Digita o KM da Viagem: '))
print('Voce vai viajar {} km'.format(km))
if km <= 200:
    v = km * 0.50
else:
    v = km * 0.45
print('O Valor de {} KM custa R${:.2f}'.format(km, v))
