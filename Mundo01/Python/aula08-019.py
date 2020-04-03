import random
j1 = input('digete o nome do aluno 1: ')
j2 = input('digite o nome do aluno 2: ')
j3 = input('digite o nome de aluno 3: ')
j4 = input('digite o nome do aluno 4: ')
alunos = (j1,j2,j3,j4)
sort = (random.choice(alunos))
print(sort)
print(f'hoje é seu dia {sort}')
