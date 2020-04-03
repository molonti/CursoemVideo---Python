num = 0
while True:
    num = int(input('Tabuada de qual valor? '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f' {c} x {num} = {c * num}')
    print('=-' * 20)