numero = int(input("Digite um número n: "))
print("A soma dos números pares compreendidos no intervalo [1; n] é: ")

numeros = range(1, numero + 1)
soma = 0

for x in numeros:
    check_par = x % 2
    if check_par == 0:
        soma = x + soma
    print(soma)


