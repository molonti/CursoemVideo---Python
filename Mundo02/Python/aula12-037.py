n = int(input('Informe um número inteiro: '))
print ('1) Converter para binário')
print ('2) Converter para octal')
print ('3) Converter para hexadecimal')
op = int(input('Digite a opção desejada: '))
if op == 1:
    print(f'{n} convertido para binário é {bin(n)[2:]}')
elif op == 2:
    print(f'{n} convertido para octal é {oct(n)[2:]}')
elif op == 3:
    print(f'{n} convertido para hexadecimal é {hex(n)[2:]}')
else:
    print('Opção inválida. Finalizando o programa.')