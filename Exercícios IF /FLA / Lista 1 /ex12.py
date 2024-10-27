# ser multiplo de 5

numero = int(input("Verifique se o número desejado é multiplo de 5: "))

conta = numero % 5

if conta == 0:
    print(f"O número {numero} é multiplo de 5")
elif conta != 0:
    print(f"O número {numero} não é multiplo de 5")
