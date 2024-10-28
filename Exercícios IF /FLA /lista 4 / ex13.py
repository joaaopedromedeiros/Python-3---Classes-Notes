
a = int(input("Digite um número para encontrar multiplos: "))
n = int(input("Quantos multiplos vc quer? "))


lista_a = []
quantidade = []

def multiplos(a,n):
    
    for x in range(1, n + 1):
        quantidade.append(x)
    print(quantidade)
    
    for valor in quantidade:
        multiplo = a * valor
        lista_a.append(multiplo)
        
    print(lista_a)
        

multiplos(a,n)
        
        

# escrever uma lista com a quantidade de
# N números que ele quer...
# a partir dos valores da lista,
# multiplica ele 
        


    
    
    