numero = int(input("Digite um número: "))

numeros = range(1, numero + 1)
produto = 1

for x in numeros:
    impar = x % 2
    if impar != 0:
        produto *= x
    
print(produto)