a = int(input("Valor A: "))
b = int(input("Valor B: "))

def divisivel(a,b):
    dividir = a % b
    if dividir == 0:
        print("True")
    else:
        print("False")

divisivel(a,b)