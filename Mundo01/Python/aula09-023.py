num = input("Digite um número: ")
num = "0" * (4 - len(num)) + num
print("Unidades: ", num[len(num) - 1])
print("Dezenas: ", num[len(num) - 2])
print("Centenas: ", num[len(num) - 3])
print("Milhar: ", num[len(num) - 4])
