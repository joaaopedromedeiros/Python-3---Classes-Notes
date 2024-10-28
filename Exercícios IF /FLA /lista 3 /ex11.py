
valor = input("Valores para lista: ")
lista = valor.split()

lista_num = []

for x in lista:
    num = int(x)
    lista_num.append(num)
    
    
    
media = sum(lista_num) / len(lista_num)

print(media)