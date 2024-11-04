numero = int(input("Digite um número para obter seus dividores inteiros na ordem crescente: "))

numeros = range(1, numero + 1)
numeros_divisiveis = []


for x in numeros:
    divisao = numero % x
    if divisao == 0:
        numeros_divisiveis.append(x)

#print(numeros_divisiveis)

# Deixando inverso
numeros_ordenados = sorted(numeros_divisiveis, reverse=True)
for numero in numeros_ordenados:
    print(numero)