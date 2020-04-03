jogador = str(input('Escolha: Pedra, Papel ou Tesoura? ')).title()
import random
lista = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(lista)
print(computador)
if computador == jogador:
      print("Empatou")
else:
      lis = [computador, jogador]
      derrota = [['Pedra', 'Tesoura'], ['Papel', 'Pedra'], ['Tesoura', 'Papel']]
      vitoria = [['Tesoura', 'Pedra'], ['Pedra', 'Papel'], ['Papel', 'Tesoura']]
      if lis in derrota:
            print("Computador Ganhou!")
      elif lis in vitoria:
          print("Você Ganhou!")
      else:
          print(f'\033[4;31m{jogador}\033[m Não existe, tente denovo !!!')
