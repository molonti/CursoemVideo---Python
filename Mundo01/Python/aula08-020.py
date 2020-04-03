import random
aluno1 = input('primeiro aluno: ')
aluno2 = input('segundo aluno: ')
aluno3 = input('terceiro aluno: ')
aluno4 = input('quarto aluno: ')
alunos = aluno1, aluno2, aluno3, aluno4
sorteio = random.sample(alunos, 4)
print(f'A ordem  de apresentação dos trabalhos será {sorteio}.')
