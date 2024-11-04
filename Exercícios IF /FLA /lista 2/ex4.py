numero = int(input("Digite um número positivo: "))
numeros = range(1, numero + 1)
produto = 1

for x in numeros:
    produto *= x

print(produto)


