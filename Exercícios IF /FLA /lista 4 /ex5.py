a = int(input("Valor A: "))
b = int(input("Valor B: "))
c = int(input("Valor C: "))

lista = []
def intervalos(a,b, c):
    for x in range(a, b + 1):
        lista.append(x)
    print(f'Intervalo: {lista}')
    if c in lista:
        print(f'O elemento {c} está na lista?')
        print(True)
    else:
        print(f'O elemento {c} está na lista?')
        print(False)
    


intervalos(a,b, c)