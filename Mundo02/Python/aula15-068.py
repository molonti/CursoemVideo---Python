from random import randint
print('=-'*17)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*17)
comp=randint(0,9)
cont=-1
while True:
    cont+=1
    pi = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    valor = int(input('Diga um valor: '))
    if pi == 'P':
        soma=valor+comp
        if soma/2 == soma//2:
            print('-'*34)
            print(f'Você jogou {valor} e o computador {comp}. Total de {soma} DEU PAR')
            print('-' * 34)
            print('Você VENCEU!!!\nVamos jogar novamente...')
            print('=-' * 17)
        else:
            print('-' * 34)
            print(f'Você jogou {valor} e o computador {comp}. Total de {soma} DEU ÍMPAR')
            print('-' * 34)
            print('Você PERDEU!!!')
            print('=-' * 17)
            print(f'Você venceu {cont} vezes.')
            break
    if pi == 'I':
        soma = valor + comp
        if soma/2 != soma//2:
            print('-' * 34)
            print(f'Você jogou {valor} e o computador {comp}. Total de {soma} DEU ÍMPAR')
            print('-' * 34)
            print('Você VENCEU!!!\nVamos jogar novamente...')
            print('=-' * 17)
        else:
            print('-' * 34)
            print(f'Você jogou {valor} e o computador {comp}. Total de {soma} DEU PAR')
            print('-' * 34)
            print('Você PERDEU!!!')
            print('=-' * 17)
            print(f'GAME OVER! Você venceu {cont} vezes.')
            break