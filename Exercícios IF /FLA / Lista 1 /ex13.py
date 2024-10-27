# informa se é multiplo de 5 e 3

valor = int(input("Verifique se o número é multiplo de 3 e 5: "))

check_5 = valor % 5
check_3 = valor % 3

if check_5 == 0:
    print(f"O número {valor} é multiplo de 5")
else:
    print(f"O número {valor} não é multiplo de 5")

if check_3 == 0:
    print(f"O número {valor} é multiplo de 3")
else:
    print(f"O número {valor} não é multiplo de 3")
