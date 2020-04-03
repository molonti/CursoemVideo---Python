Tgasto = Amil = NomeP = valorP = 0
while True:
    print('-='*20,'\n Compra de produtos\n','-='*20)
    n = str(input('Digite o nome do produto '))
    p = float(input('Preço R$ '))
    if valorP == 0:
        valorP = p
        NomeP = n
    elif valorP > p:
        valorP = p
        NomeP = n
    Tgasto += p
    if p >= 1000:
        Amil += 1
    t = str(input('Deseja continuar [S/N] >>>')).strip().upper()
    if t == 'N':
        print('O programa foi encerrado com sucesso')
        break
print(f'Total de gasto foi : {Tgasto}\n Produto acima de 1000 reais {Amil} produtos')
print(f'O produto mais barato foi {NomeP} que foi R${valorP:.2f}')
