i = 0

while i == 0:
    try:
        numero = int(input("Digite um número para dobra-lo: "))
        if numero == 0:
            raise ValueError()
        dobrar = numero * 2
        print(dobrar)
        i = 1
    except ValueError as e:
        print(e)
        
        