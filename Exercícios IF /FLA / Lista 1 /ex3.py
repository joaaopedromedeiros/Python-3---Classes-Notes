i = 0

while i == 0:
    try:
        numero_1 = float(input("Digite 1 número: "))
        numero_2 = float(input("Digite outro número: "))
        numero_3 = float(input("Digite outro número: "))
        
        soma = numero_1 + numero_2 + numero_3
        print(soma/3)
        
        
    except ValueError as e:
        print("Vc digitou algum valor invalido")
        
        