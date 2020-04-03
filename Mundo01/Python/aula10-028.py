import random
num =random.randint(1,5)
num1 = int(input('qual é o numero? '))
if num1==num:
    print('Ganhou')
else:
    print ('Perdeu')
print(num)