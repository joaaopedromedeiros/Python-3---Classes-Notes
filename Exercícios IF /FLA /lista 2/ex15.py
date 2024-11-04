numero = int(input("Digite um número: "))

numeros = range(1, numero + 1)
soma = 0
lista = []

for x in numeros:
    soma = soma + x

for numero in numeros:
    lista.append(numero)



for valor in lista:
    print(valor)


print(soma)

