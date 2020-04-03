v = float(input('Digite a Velocidade do Carro: '))
if v > 80:
    print('MULTADO, excedeu o limite de 80KM ')
    multa = (v - 80) * 7
    print('Valor da MULTA R$ {:.2f}'.format(multa))
print('Bom dia, Dirija com segurança: ')
