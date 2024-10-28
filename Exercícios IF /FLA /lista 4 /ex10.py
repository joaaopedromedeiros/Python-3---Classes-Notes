a = int(input("Faça a contagem de números até: "))


lista = []

def contagem(a):
    for x in range(1, a + 1):
        print(x)
        lista.append(x)
        print(lista)
    print("Resultado final: ")
    print(lista)
        

contagem(a)