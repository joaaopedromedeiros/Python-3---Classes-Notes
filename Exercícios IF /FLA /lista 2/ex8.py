

validação = 1
tentativas = 0

while validação != 0:
    numero = int(input("Digite um valor: "))

    if numero == 0:
        print("Parabéns você acertou o número desejado! ")
        validação = 0
        print(f"Você precisou de {tentativas} tentativas")
    else:
        print("Você errou o número desejado, tente novamente")
        tentativas += 1
        
    




# digitei 10 números até digitar 0, imprimi 10 tentativas....
