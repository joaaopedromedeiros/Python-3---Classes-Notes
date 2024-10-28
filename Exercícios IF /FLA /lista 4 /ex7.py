
# True --> par , False --> impar 

a = int(input("Valor a: "))
b = int(input("Valor b: "))

def parimpar(a,b):
    parA = a % 2
    parB = b % 2
    
    if parA == 0:
        print("True")
    else:
        print("False")
    if parB == 0:
        print("True")
    else: 
        print("False")


parimpar(a,b)
    