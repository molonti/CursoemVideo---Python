valor = float(input('Digite o valor do produto: '))
print('A vista no dinheiro:(1)')
print('A vista no cartao:  (2)')
print('Parcelado até 2x:   (3)')
print('Parcelado 3x ou +   (4)')
opcao = int(input(''))
if opcao == 1:
    result = valor-((valor/100)*10)
    print(f'O valor total é R${result}')
elif opcao == 2:
    result = valor - ((valor / 100) * 5)
    print(f'O valor total é R${result}')
elif opcao == 3:
    result = valor/2
    print(f'Você pagará 2x de R${result}')
elif opcao == 4:
    parcela = int(input('Deseja dividir em quantas vezes? '))
    result = valor + ((valor / 100) * 20)
    valor_parcela = result / parcela
    print(f'Você irá pagar {parcela}x de  R${valor_parcela}')
    print(f'Valor do juros por mês: R${(valor/100)*20/parcela}')
    print(f'Valor total: R${result}')
else:
    print('Opção invalida! ')