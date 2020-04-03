altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / (altura * altura)
print(f'O seu Índice de Massa Corpórea (IMC) é {imc:.4f} ')
if imc < 18.5:
    print('IMC = {:.2f} Você está abaixo do peso'.format(imc))
elif 18.6 <= imc <= 25:
    print('IMC = {:.2f} Você está com peso ideal'.format(imc))
elif 25.1 <= imc <= 30:
    print('IMC = {:.2f} Você está com sobrepeso'.format(imc))
elif 30.1 <= imc <= 40:
    print('IMC = {:.2f} Você esta obeso(a)'.format(imc))
elif 40.1 <= imc:
    print('IMC = {:.2f} Obesidade Mórbida'.format(imc))