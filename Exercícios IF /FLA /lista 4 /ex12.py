n = int(input("Quantos multiplos de 3 você deseja? "))

lista = []


def multiplos3(n):
    for x in range(1,n + 1):
        print(x)
        multiplo = 3 * x
        lista.append(multiplo)
    print(lista)
        

multiplos3(n)
