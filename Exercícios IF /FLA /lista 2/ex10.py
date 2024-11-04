
validação = 1

while validação != 0:
    numero = int(input("Digite um número para achar a sua raiz: "))

    if numero < 0:
        print("Você digitou um valor negativo, repita a leitura ")
        continue
    else: 
        raiz = numero ** 0.5
        print(f"A raiz quadrada de {numero} é {raiz}")
        validação = 0




