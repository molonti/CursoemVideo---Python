n = 0
s = 0
c = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores é {s}')


