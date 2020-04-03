v = int(input('Digite uma Velocidade: '))
multa = ((v - 80) * 7)
if v > 80:
    print(f'Voce foi multado: {(v - 80 ) * 7}')
else:
    print('Obrigado')