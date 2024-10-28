a = int(input("Defina até qual número vc deseja ver os pares compreendidos no intervalo: "))

lista_pares = []

def pares(a):
    for x in range(0, a + 1,2):
        print(x)
        lista_pares.append(x)
        print(lista_pares)
    print("Resultado final: ")
    print(lista_pares)

pares(a)

