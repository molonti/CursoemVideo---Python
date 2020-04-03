n1 = float(input('Informe o primeiro segmento: '))
n2 = float(input('Informe o segundo segmento: '))
n3 = float(input('Informe o terceiro segmento: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n1 + n2:
    print('Os segmentos informados FORMAM um triângulo ')
if n1 == n2 == n3:
    print ('EQUILÁTERO.')
elif n1 != n2 != n3 != n1:
    print ('ESCALENO.')
else:
    print ('ISÓSCELES.')