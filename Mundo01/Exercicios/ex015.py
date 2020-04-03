dias = int(input('Quantos dias: '))
km = float(input('Quantos KM: '))
pago = (dias * 60) + (km * 0.15)
print('Total a pagar por Dia {:.2f}'.format(pago))

