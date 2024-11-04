numero = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))

print(f" A soma dos números no intervalo de [{numero}:{numero2}] é:  ")

valores = range(numero, numero2 + 1)
soma = 0
for x in valores:
    soma += x

print(soma)