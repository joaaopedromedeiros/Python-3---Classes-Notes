

validação = 1
soma_total = 0

while validação != 0:
    numero = int(input("Digite um número: "))

    if numero == 0:
        print("Parabéns vocêacertou o valor desejado!")
        print(soma_total)
        validação = 0
    else:
        print("Você errou o valor desejado tente novamente...")
        soma_total += numero
    
