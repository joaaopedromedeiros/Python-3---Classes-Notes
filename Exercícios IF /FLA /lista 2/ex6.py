numero = int(input("Digite um número: "))

numeros = range(1, numero + 1)
print(numeros)

soma_par = 0
soma_impar = 0

for x in numeros:
    par_ou_impar = x % 2
    if par_ou_impar == 0:
        soma_par = x + soma_par
    if par_ou_impar != 0:
        soma_impar = x + soma_impar

print(f"Soma dos números impares: {soma_impar}")
print(f"Soma dos números pares: {soma_par}")

#1
#2
#3
#4
#5
#6

# 12 par
# 9 impar 
